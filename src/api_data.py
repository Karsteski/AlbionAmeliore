import requests
from typing import Any

from items import *

API_HOST_URL = "https://west.albion-online-data.com"
ENDPOINT = "/api/v2/stats/prices/"

item_info = "T3_FARM_WHEAT_SEED?locations=&qualities=0"


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


def getCurrentPrices(items: list[Item], 
                     cities: list[City],
                     qualities: list[Quality] = [Quality.Non]) \
-> list[dict[str,Any]]:
    """
    """

    request = buildRequest(API_HOST_URL, ENDPOINT, items, cities, qualities)

    print("Request = ", request)

    response = requests.get(request)

    if response.status_code == 200:
        data = response.json()
        return data 
    else:
        print("Error:", response.status_code)
        return [{}]




def marketResponsetoMarketData(response: list[dict[str, Any]]) \
    -> list[MarketData]:
    """
    """

    market_data : list[MarketData] = []
    
    for market_response_data in response:
        # TODO: should be wrapped in try-except
        item_data = MarketData(
            item = Item(name = market_response_data["item_id"],
                        uid = market_response_data["item_id"],
                        quality= Quality(market_response_data["quality"])
            ),
            city = market_response_data["city"],

            min_sell_price=market_response_data["sell_price_min"],
            max_sell_price=market_response_data["sell_price_max"],

            min_buy_price=market_response_data["buy_price_min"],
            max_buy_price=market_response_data["buy_price_max"],
        )

        market_data.append(item_data)
    
    
    return market_data















