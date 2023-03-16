"""
Practical Use Decorators
author: Jacob York
"""
from datetime import datetime


def log_error(function):
    """logs all Exceptions during function into a file called error_log.txt."""
    def inner(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as e:
            with open("error_log.txt", "a") as error_file:
                error_file.write(f"{datetime.now()} {type(e)}: {e}\n")
            
    return inner


def ignore_if_error(function):
    """Skips the function if there is any error."""
    def inner(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except:
            pass
    return inner


def method_expects(*param_types):
    """Used with METHOD definitions to restrict the parameter to param_type.
    Does not support functions."""
    def decorator(function):
        def inner(self, *args):
            for i in range(len(param_types)):
                if not isinstance(args[i], param_types[i]):
                    raise TypeError(f'"{args[i]}" of type {type(args[i])} must be of type {param_types[i]}.')
            function(self, *args)
        return inner
    return decorator


def expects(*param_types):
    """Used with functions."""
    def decorator(function):
        def inner(*args):
            for i in range(len(param_types)):
                if not isinstance(args[i], param_types[i]):
                    raise TypeError(f'"{args[i]}" of type {type(args[i])} must be of type {param_types[i]}.')
            function(*args)
        return inner
    return decorator
