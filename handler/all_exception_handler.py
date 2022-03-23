from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response


class AllExceptionHandler(AbstractExceptionHandler):
    
    def can_handle(self, handler_input: HandlerInput, exception: Exception) -> bool:
        return True
    
    def handle(self, handler_input: HandlerInput, exception: Exception) -> Response:
        
        print(exception)
        
        speech = "すみません、わかりませんでした。もう一度言ってください。"
        
        (
            handler_input.response_builder
            .speak(speech)
            .ask(speech)
        )
        
        return handler_input.response_builder.response
