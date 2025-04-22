from google.adk.tools import LongRunningFunctionTool


def my_long_task_generator(*args, **kwargs):
    # ... setup ...
    yield {
        "status": "pending",
        "message": "Starting task...",
    }  # Framework sends this as FunctionResponse
    # ... perform work incrementally ...
    yield {
        "status": "pending",
        "progress": 50,
    }  # Framework sends this as FunctionResponse
    # ... finish work ...
    return {
        "status": "completed",
        "result": "Final outcome",
    }  # Framework sends this as final FunctionResponse


my_tool = LongRunningFunctionTool(func=my_long_task_generator)
