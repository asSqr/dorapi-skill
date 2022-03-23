from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_type
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard


class HelpIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_type("AMAZON.HelpIntent")(handler_input)
    
    def handle(self, handler_input: HandlerInput) -> Response:
        speech_text = "こんにちは。と言ってみてください。"
        
        (
            handler_input.response_builder
            .speak(speech_text)
            .ask(speech_text)
            .set_card(SimpleCard("ハローワールド", speech_text))
        )
        
        return handler_input.response_builder.response
