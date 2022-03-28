from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name, get_slot_value
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import StandardCard, Image

from constants.alexa_skill import (
    DORAPI_GADGET_SLOT,
    DORAPI_SPEECH_TEXT,
    DORAPI_CARD_TITLE,   
)
from api.dorapi import get_gadget_names_by_keyword
from api.custom_search import get_image_url_from_google

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class DorapiIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("DorapiIntent")(handler_input)
    
    def handle(self, handler_input: HandlerInput) -> Response:
        logger.info('In DorapiIntentHandler')
        
        gadget_keyword = get_slot_value(handler_input, DORAPI_GADGET_SLOT)
        
        gadget_name = get_gadget_names_by_keyword(gadget_keyword)[0]
        
        image_url = get_image_url_from_google(gadget_name)
        image = Image(
            small_image_url=image_url,
            large_image_url=image_url
        )
        
        speech_text = DORAPI_SPEECH_TEXT.format(gadget_keyword, gadget_name)
        card_title = DORAPI_CARD_TITLE.format(gadget_keyword)
        
        (
            handler_input.response_builder
            .speak(speech_text)
            .set_card(StandardCard(
                title=card_title,
                text=gadget_name,
                image=image
            ))
            .set_should_end_session(True)
        )
        
        return handler_input.response_builder.response
