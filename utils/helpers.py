import requests

from http import HTTPStatus
from typing import Optional


def verify_links(links: Optional[list]) -> list:
    _total_links = len(links)
    _total_broken_links = 0
    _broken_links = []
    _result = dict()
    
    if _total_links == 0:
        return {
            'total_links': 0,
            'total_valid_links': 0,
            'total_broken_links': _total_broken_links,
            'broken_links': _broken_links
        }

    for link in links:
        response = requests.get(link)
        if response.status_code >= HTTPStatus.BAD_REQUEST:
            _total_broken_links += 1
            _broken_links.append(link)
        
    _total_valid_links = _total_links - _total_broken_links
    
    _result = {
        'total_links': _total_links,
        'total_valid_links': _total_valid_links,
        'total_broken_links': _total_broken_links,
        'broken_links': _broken_links
    }

    return _result

def get_value(key: str, source: dict):
        if not isinstance(source, dict):
            raise ValueError(f'Source is not a valid dict type')
        
        if key not in list(source.keys()):
            raise ValueError(f'Not found key: {key} in source: {source}')
        
        return source[key]

def get_enum_values(enum):
    return [e.value for e in enum]

def sorted_list(items: list, reverse=False):
    if reverse:
        return all(items[i] >= items[i+1] for i in range(len(items) - 1))

    return all(items[i] <= items[i+1] for i in range(len(items) - 1))




