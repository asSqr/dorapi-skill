from ask_sdk_core.dispatch_components import AbstractRequestInterceptor

import logging

logger = logging.getLogger(__name__)


class LogRequestInterceptor(AbstractRequestInterceptor):
    
    def process(self, handler_input):
        logger.info(f"Request type: {handler_input.request_envelope.request.object_type}")
