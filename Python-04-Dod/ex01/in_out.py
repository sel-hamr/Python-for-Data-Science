def square(x: int | float) -> int | float:
    """square(x: int | float) -> int | float that returns the square of x."""
    return x * x

def pow(x: int | float) -> int | float:
    """pow(x: int | float) -> int | float that returns x raised to the power of x."""
    return x ** x

def outer(x: int | float, function) -> object:
    """outer(x: int | float, function) -> object that returns a function that takes no arguments and returns the result of applying function to x."""
    count = 0
    def inner() -> float:
        """inner() -> float that returns the result of applying function to x."""
        nonlocal count
        count = count if count != 0 else x
        count = function(count)
        return count
    return inner
