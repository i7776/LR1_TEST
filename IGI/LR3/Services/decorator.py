def log_decorator(func):
    """
    Decorator to log the start and end of a function
    :param func: the function to be decorated
    :return: new function
    """
    def new_func (*args, **kwargs):
        print(f"\n[LOG] Function is executing: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Function {func.__name__} ended.")
        return result
    return new_func