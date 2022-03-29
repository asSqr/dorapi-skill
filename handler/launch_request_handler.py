from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_request_type("LaunchRequest")(handler_input)
    
    def handle(self, handler_input: HandlerInput) -> Response:
        logger.info('In LaunchRequestHandler')
        
        card_title = "ドラピアイ"
        speech_text = "ようこそ、ドラピアイへ。ひみつ道具に関するキーワードを言ってみてください。"
        
        (
            handler_input.response_builder
            .speak(speech_text)
            .set_card(SimpleCard(card_title, speech_text))
            .set_should_end_session(False)
        )
        
        return handler_input.response_builder.response
