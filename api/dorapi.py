from constants.dorapi import (
    DORA_BASE_URL, DORA_GADGETS_PATH,
    DORA_GADGET_PAGE, DORA_GADGET_PAGE_SIZE,
)
from utils import generate_query

import requests
from urllib.parse import quote
from typing import List

import logging


logger = logging.getLogger(__name__)


def get_gadget_names_by_keyword(keyword: str) -> List[str]:
    query_dict = {
        'keyword': quote(keyword),
        'page': DORA_GADGET_PAGE,
        'page_size': DORA_GADGET_PAGE_SIZE,
    }
    
    query = generate_query(query_dict)
    
    url = f'{DORA_BASE_URL}{DORA_GADGETS_PATH}?{query}'
    
    logger.info('[get_gadget_names_by_keyword] {}', url)
    
    resp = requests.get(url).json()
    gadgets = resp['datas']
    
    gadget_name_list = []
    
    for gadget in gadgets:
        gadget_name_list.append(gadget['name'])

    return gadget_name_list
