from ask_sdk_core.skill_builder import SkillBuilder

from .handler import (
    AllExceptionHandler,
    CancelAndStopIntentHandler,
    DorapiIntentHandler,
    HelpIntentHandler,
    LaunchRequestHandler,
    SessionEndedRequestHandler,
)


skill_builder = SkillBuilder()

skill_builder.add_request_handler(LaunchRequestHandler())
skill_builder.add_request_handler(DorapiIntentHandler())
skill_builder.add_request_handler(HelpIntentHandler())
skill_builder.add_request_handler(CancelAndStopIntentHandler())
skill_builder.add_request_handler(SessionEndedRequestHandler())

skill_builder.add_exception_handler(AllExceptionHandler())

handler = skill_builder.lambda_handler()
