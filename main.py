from fastapi import FastAPI
from models import Item
from parser import parser

# SWIGGY IMPORTS
from request import *
import json
from curl_cffi import requests
import jmespath

app = FastAPI()


# ======================================
# HOME API
# ======================================

@app.get("/")
def home():

    return {
        "message": "Welcome to the Top 10 Restaurants API!"
    }


# ======================================
# COMBINED API
# ======================================

@app.post("/restaurants")
def get_top_restaurants(item: Item):

    # ======================================
    # ZOMATO
    # ======================================

    city = item.city
    dish_name = item.dish_name

    zomato_url = f"https://www.zomato.com/{city}/delivery/dish-{dish_name.replace(' ', '-')}"

    get_id = f"/{city}/delivery/dish-{dish_name.replace(' ', '-')}"

    print("ZOMATO URL :", zomato_url)

    zomato_data = parser(zomato_url, get_id)

    # ======================================
    # SWIGGY
    # ======================================

    swiggy_restaurants = []

    try:

        # CITY SEARCH
        json_data = {
            'input': item.city,
            'types': [],
            '_csrf': 'gtRGh1quhUpu-LLsSKvHY8XVpdCBWmvM1R85eKSw',
        }

        response = requests.post(
            AUTOCOMPLETE_URL,
            headers=headers,
            json=json_data,
            impersonate="chrome120"
        )

        print("AUTOCOMPLETE STATUS :", response.status_code)

        if response.status_code == 200:

            response_json = response.json()

            if response_json.get("data"):

                place_id = response_json.get("data")[0].get("place_id")

                print("PLACE ID :", place_id)

                if place_id:

                    # LOCATION API
                    json_data = {
                        'place_id': place_id,
                        '_csrf': 'wx7h9qXtQHeI-kcHvcFh74k93-3FLNJfw3NIR7HQ',
                    }

                    response_lt = requests.post(
                        ADDRESS_RECOMMEND,
                        headers=headers,
                        json=json_data,
                        impersonate="chrome120"
                    )

                    print("LOCATION STATUS :", response_lt.status_code)

                    if response_lt.status_code == 200:

                        location_data = response_lt.json()

                        if location_data.get("data"):

                            location = (
                                location_data
                            ).get("data")[0].get("geometry").get("location")

                            print("LOCATION :", location)

                            if location:

                                lat = location.get("lat")
                                lng = location.get("lng")

                                # ITEM SUGGESTION
                                params = {
                                    'lat': lat,
                                    'lng': lng,
                                    'str': item.dish_name,
                                    'trackingId': 'e2a82109-0cd2-50ad-b641-c895066acf14',
                                    'includeIMItem': 'true',
                                }

                                response_item_suggestion = requests.get(
                                    ITEM_SEARCH_SUGGESTION,
                                    params=params,
                                    headers=headers,
                                    impersonate="chrome120"
                                )

                                print(
                                    "ITEM SUGGESTION STATUS :",
                                    response_item_suggestion.status_code
                                )

                                if response_item_suggestion.status_code == 200:

                                    suggestion_json = response_item_suggestion.json()

                                    suggestions = (
                                        suggestion_json
                                        .get("data", {})
                                        .get("suggestions", [])
                                    )

                                    if suggestions:

                                        first_suggestion = suggestions[0]

                                        item_name = first_suggestion.get("text")

                                        metaData = json.loads(
                                            first_suggestion.get("metadata")
                                        )

                                        print("ITEM NAME :", item_name)

                                        # RESTAURANT SEARCH
                                        params = {
                                            'lat': lat,
                                            'lng': lng,
                                            'str': item_name,
                                            'trackingId': 'e2a82109-0cd2-50ad-b641-c895066acf14',
                                            'submitAction': 'SUGGESTION',
                                            'queryUniqueId': '110048ea-6861-2404-5e28-22565dfba13b',
                                            'metaData': metaData,
                                            'selectedPLTab': 'RESTAURANT',
                                        }

                                        response_restaurant_list = requests.get(
                                            RESTAURANT_SEARCH,
                                            params=params,
                                            headers=headers,
                                            impersonate="chrome120"
                                        )

                                        print(
                                            "RESTAURANT STATUS :",
                                            response_restaurant_list.status_code
                                        )

                                        if response_restaurant_list.status_code == 200:
                                            with open('swiggy_response.json', 'w') as f:
                                                json.dump(
                                                    response_restaurant_list.json(),
                                                    f,
                                                    indent=4
                                                )
                                            restaurants = jmespath.search(
                                                "data.cards[0].groupedCard.cardGroupMap.RESTAURANT.cards[*].card.card.info",
                                                response_restaurant_list.json()
                                            )
                                            swiggy_restaurants = []

                                            for restaurant in restaurants:

                                                swiggy_restaurants.append({

                                                    "res_id": restaurant.get("id"),

                                                    "res_name": restaurant.get("name"),

                                                    "res_rating": restaurant.get("avgRatingString"),

                                                    "address": restaurant.get("address")

                                                })

    except Exception as e:

        print("SWIGGY ERROR :", e)


    return {

        "city": item.city,

        "dish_name": item.dish_name,

        "zomato_restaurants": zomato_data,

        "swiggy_restaurants": swiggy_restaurants[:10]
    }