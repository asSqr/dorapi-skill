# coding: utf-8

from ask_sdk_core.skill_builder import SkillBuilder

from handler import (
    AllExceptionHandler,
    CancelAndStopIntentHandler,
    DorapiIntentHandler,
    HelpIntentHandler,
    LaunchRequestHandler,
    SessionEndedRequestHandler,
)

from interceptor import (
    LogRequestInterceptor
)


skill_builder = SkillBuilder()

skill_builder.add_request_handler(LaunchRequestHandler())
skill_builder.add_request_handler(DorapiIntentHandler())
skill_builder.add_request_handler(HelpIntentHandler())
skill_builder.add_request_handler(CancelAndStopIntentHandler())
skill_builder.add_request_handler(SessionEndedRequestHandler())

skill_builder.add_exception_handler(AllExceptionHandler())

skill_builder.add_global_request_interceptor(LogRequestInterceptor())


handler = skill_builder.lambda_handler()
