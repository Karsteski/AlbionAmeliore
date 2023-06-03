import json 
from typing import Any
from fuzzysearch import find_near_matches

from items import Item


def getFileKeyValueData(filename: str) -> dict[str, str]:
    """
    Expects file with 3 values separated by two colons
    E.g  items.txt from ao-bin-dumps
    """

    result: dict[str, str] = {}

    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            data = line.split(":")

            try:
                key = data[1] # UID
                value = data[2] # Name

                tidied_key = key.strip()
                tidied_key = tidied_key.rstrip('\n')

                tidied_value = value.strip()

                result[tidied_key] = tidied_value
            except IndexError:
                # Some unimportant items have non-conforming formats
                pass

    return result

def stringsToItems(item_strings : dict[str,str]) -> list[Item]:
    items: list[Item] = []

    for key, value in item_strings.items():
        items.append(Item(value, key))

    return items

def findNearestItemNames(
        items: list[Item],
        string_to_match: str,
        max_num_of_names: int = 5) -> set[str]:
    matches = set()
    
    MAX_DISTANCE = 2
    for item in items:
        near_matches = find_near_matches(string_to_match,
                            item.name, max_l_dist=MAX_DISTANCE)
    
        if near_matches:
            matches.add(item.name)

    return matches
