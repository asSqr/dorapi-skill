from constants.dorapi import (
    DORA_BASE_URL, DORA_GADGETS_PATH,
    DORA_GADGET_PAGE, DORA_GADGET_PAGE_SIZE,
)
from utils import generate_query

import requests
from typing import List


def get_gadget_names_by_keyword(keyword: str) -> List[str]:
    query_dict = {
        'keyword': keyword,
        'page': DORA_GADGET_PAGE,
        'page_size': DORA_GADGET_PAGE_SIZE,
    }
    
    query = generate_query(query_dict)
    
    url = f'{DORA_BASE_URL}{DORA_GADGETS_PATH}?{query}'
    
    resp = requests.get(url)
    gadgets = resp['datas']
    
    gadget_name_list = []
    
    for gadget in gadgets:
        gadget_name_list.append(gadget['name'])

    return gadget_name_list
