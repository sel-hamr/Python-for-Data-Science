def ft_filter(fn,list):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true"""
    return [item for item in list if fn(item)]
