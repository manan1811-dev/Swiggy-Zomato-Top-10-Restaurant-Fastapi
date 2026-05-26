from lxml import html
from request import *
import re
import json

def get_page_json(url):
    data = request(url)
    tree = html.fromstring(data)
    script = tree.xpath("//script/text()")
    for s in script:
        if 'window.__PRELOADED_STATE__' in s[:1000]:
            match = re.search(r'JSON\.parse\("(.*)"\)', s)
            json_str = match.group(1)
            json_str = json_str.encode().decode('unicode_escape')
            break
    return json_str

def parser(url,get_id):
    json_str = get_page_json(url)
    data= json.loads(json_str)

    zomato_restaurants = []
    
    all_data = data.get('pages').get('search').get(get_id).get('sections').get("SECTION_SEARCH_RESULT")
    for a in all_data:
        zomato_restaurants.append({
            "res_id": a.get('info').get('resId'),
            "res_name": a.get('info').get('name'),
            "res_rating": a.get('info').get('rating').get('aggregate_rating'),
            "address": a.get('info').get('locality').get('address'),

        })

    with open('name.json', 'w') as f:
        json.dump(data, f, indent=4)
    return zomato_restaurants