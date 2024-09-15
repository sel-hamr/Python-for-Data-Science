from typing import Any

def callLimit(limit: int):
    """callLimit(limit) -> function that limits the number of calls to the function it decorates to the value of limit."""
    count = 0
    def callLimiter(function):
        """callLimiter(function) -> function that limits the number of calls to the function it decorates to the value of limit."""
        def limit_function(*args: Any, **kwds: Any):
            """limit_function(*args: Any, **kwds: Any) -> function that limits the number of calls to the function it decorates to the value of limit."""
            nonlocal count
            if count == limit:
                print(f"Error: {function}> call too many times")
            else :
                count+=1
                function()
        return limit_function
    return callLimiter