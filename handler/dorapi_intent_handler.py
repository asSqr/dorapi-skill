from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_type
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard


class DorapiIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_type("DorapiIntent")(handler_input)
    
    def handle(self, handler_input: HandlerInput) -> Response:
        speech_text = "こんにちは"
        
        (
            handler_input.response_builder
            .speak(speech_text)
            .set_card(SimpleCard("ハローワールド", speech_text))
            .set_should_end_session(True)
        )
        
        return handler_input.response_builder.response
