from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class SessionEndedRequestHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("SessionEndedRequest")(handler_input)
    
    def handle(self, handler_input: HandlerInput) -> Response:
        logger.info('In SessionEndedRequestHandler')
        
        return handler_input.response_builder.response
