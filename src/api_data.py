import json
import requests

from items import *

API_HOST_URL = "https://west.albion-online-data.com"
ENDPOINT = "/api/v2/stats/prices/"

item_info = "T3_FARM_WHEAT_SEED?locations=&qualities=0"


def getCurrentPrices(items: list[Item], 
                     cities: list[City],
                     qualities: list[Quality] = [Quality.Non]):


    request = buildRequest(API_HOST_URL, ENDPOINT, items, cities, qualities)

    print("Request = ", request)

    response = requests.get(request)

    if response.status_code == 200:
        data = response.json()
        return data 
    else:
        print("Error:", response.status_code)
        return ""


def buildRequest(api_host_url: str,
                 api_endpoint: str,
                 items: list[Item],
                 cities: list[City],
                 qualities: list[Quality]) -> str:
                
    request = api_host_url + \
        api_endpoint + \
        ",".join(item.uid for item in items) + \
        "?locations=" + \
        ",".join(city.name for city in cities) + \
        "&qualities="+ \
        ",".join(str(quality.value) for quality in qualities)

    return request
