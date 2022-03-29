from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class HelpIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("AMAZON.HelpIntent")(handler_input)
    
    def handle(self, handler_input: HandlerInput) -> Response:
        logger.info('In HelpIntentHandler')
        
        card_title = "ドラピアイ"
        speech_text = "ひみつ道具に関するキーワードを言ってみてください。"
        
        (
            handler_input.response_builder
            .speak(speech_text)
            .ask(speech_text)
            .set_card(SimpleCard(card_title, speech_text))
        )
        
        return handler_input.response_builder.response
