from constants.google_custom_search import (
    GOOGLE_BASE_URL, GOOGLE_CUSTOM_SEARCH_PATH,
)
from utils import generate_query

import os
import requests


def get_image_url_from_google(gadget_name: str) -> str:
    
    CSE_ID = os.getenv('CSE_ID')
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    
    query_dict = {
        'q': gadget_name.replace(' ', '+'),
        'searchType': 'image',
        'cx': CSE_ID,
        'key': GOOGLE_API_KEY,
        'start': 1,
        'lr': 'lang_ja',
        'num': 1,
    }
    
    query = generate_query(query_dict)
    
    url = f'{GOOGLE_BASE_URL}{GOOGLE_CUSTOM_SEARCH_PATH}?{query}'
    
    resp = requests.get(url).json()
    images = resp['items']
    
    return images[0]['link']
