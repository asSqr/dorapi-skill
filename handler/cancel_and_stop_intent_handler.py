from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CancelAndStopIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return (
            is_intent_name("AMAZON.CancelIntent")(handler_input)
            or is_intent_name("AMAZON.StopIntent")(handler_input)
        )
    
    def handle(self, handler_input: HandlerInput) -> Response:
        logger.info('CancelAndStopIntentHandler')
        
        speech_text = "さようなら"
        
        (
            handler_input.response_builder
            .speak(speech_text)
            .set_card(SimpleCard("ハローワールド", speech_text))
            .set_should_end_session(True)
        )
        
        return handler_input.response_builder.response
