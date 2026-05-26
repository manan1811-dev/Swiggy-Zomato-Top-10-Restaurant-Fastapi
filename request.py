from curl_cffi import requests as re

def request(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
        # 'cookie': 'PHPSESSID=6fe128531e0f4aad773e880cb969289e; csrf=0da55ef6665e4887c1bb89ff056c0e3c; fre=0; rd=1380000; zl=en; fbtrack=1ccb6e57c5c30dd0db83535a895cd21a; ak_bmsc=152C15788FAFE57FEB9F3320F69D4904~000000000000000000000000000000~YAAQMxzFF2cB6yieAQAAt07KYh8jWpxfZE3kmqHHTBXoKLmVF+iViTbzmkkagCx/LAq6HobobFw1fti7QrpDZfzxWzfgK5DKPQ2F8GMczdYaojfaqX7t+HE/Lkd2zcs4JRJaRm+Cd/ut+4hT32caWw+h86/uPzsnPKhGbqHYvwjhbq1x52uu4VeDVrwvWow6c5/xfzj2Up2cGvSvDcLhuO8Q1UQ4jZS3gYxh7y9EWU5JGn97i9ykf5aw72cu00eFerp+vwc9lUK0HIj5vNfsTN4Ipg4FRqHkYr+mWenyJ91Pxadqk9sWZd/sgyZ94lOEDmMFz25aeRcOmUMpYv1+aDtBvHBgBCvQ8EbBKOZMAP+6Tdrn2BSXisQ7MBFYIkXDZC23Gya5qxIUJVtt; _gid=GA1.2.1193710019.1779773887; expab=1; session_id=3779773ba6792-83bd-481f-b96d-6b3ca268c8e5; _fbp=fb.1.1779773886915.587586527196011226; _gcl_au=1.1.173418253.1779773887; dpr=2; _ga_2NKE6R5GNY=GS2.2.s1779773887$o1$g1$t1779774671$j13$l0$h0; fbcity=12045; ltv=12045; lty=12045; locus=%7B%22addressId%22%3A0%2C%22lat%22%3A22.73509%2C%22lng%22%3A72.44008%2C%22cityId%22%3A12045%2C%22ltv%22%3A12045%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A65864%2C%22fen%22%3A%22Dholka%22%7D; _ga_2XVFHLPTVP=GS2.1.s1779773887$o1$g1$t1779774753$j23$l0$h0; _ga=GA1.1.1089543373.1779773887; _ga_X6B66E85ZJ=GS2.2.s1779773887$o1$g1$t1779774753$j25$l0$h0; g_state={"i_l":0,"i_ll":1779774753392,"i_b":"2OpNBMKSEUAE4v5Hwr8/FfVy/JfsfBM8DNXLYbMO7eQ","i_e":{"enable_itp_optimization":0},"i_et":1779773908718}; AWSALBTG=AIeZI5JXkOXmUoQLMwz6c+tLxYtKIaNbj1WLSXdpxv3hrrJrM5LEtClbnTvAxsfi3l6emBkZmHxiE9qUK/O7n56j9+T+fnHKHHV3KJnjn0oIuTS8gSn5jYSWPH6mIW48yNHFA5njl1FFDtHBRK9lu7UBJNGwmwTyiVxThXFFqvB4; AWSALBTGCORS=AIeZI5JXkOXmUoQLMwz6c+tLxYtKIaNbj1WLSXdpxv3hrrJrM5LEtClbnTvAxsfi3l6emBkZmHxiE9qUK/O7n56j9+T+fnHKHHV3KJnjn0oIuTS8gSn5jYSWPH6mIW48yNHFA5njl1FFDtHBRK9lu7UBJNGwmwTyiVxThXFFqvB4; _dd_s=aid=2ee63348-bee2-458b-b527-1583338eb845&rum=0&expire=1779776280186',
    }

    response = re.get(url, headers=headers,impersonate="chrome120")
    print(response.status_code)
    try:
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"Error: {e}")
        return None
    
headers = {

    '__fetch_req__': 'true',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.swiggy.com',
    'platform': 'dweb',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.swiggy.com/',

    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',

    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',

    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36',

    'user-id': '0',
}


# =========================================
# SWIGGY URLS
# =========================================

AUTOCOMPLETE_URL = "https://www.swiggy.com/dapi/misc/place-autocomplete"

ADDRESS_RECOMMEND = "https://www.swiggy.com/mapi/misc/address-recommend"

ITEM_SEARCH_SUGGESTION = "https://www.swiggy.com/mapi/restaurants/search/suggest"

RESTAURANT_SEARCH = "https://www.swiggy.com/mapi/restaurants/search/v3"