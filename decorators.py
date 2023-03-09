"""
Practical Use Decorators
@author Jacob York
"""
from datetime import datetime


def log_error(function):
    """logs all Exceptions during function into a file called error_log.txt."""

    def inner(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as e:
            with open("error_log.txt", "a") as error_file:
                error_file.write(str(datetime.now()) + " " + str(type(e)) + ": " + str(e) + "\n")
            
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
    def decorator(function):
        """Used with METHOD definitions to restrict the parameter to param_type.
        Does not support functions."""
        def inner(self, *args):
            for i in range(len(param_types)):
                arg = args[i]
                param_type = param_types[i]
                if not isinstance(arg, param_type):
                    raise TypeError(
                        "\"" + str(arg) + "\" of type " + str(type(arg)) + " must be of type " + str(param_type) + "."
                    )
            function(self, *args)
        return inner
    return decorator


def expects(*param_types):
    def decorator(function):
        """Used with functions."""
        def inner(*args):
            for i in range(len(param_types)):
                arg = args[i]
                param_type = param_types[i]
                if not isinstance(arg, param_type):
                    raise TypeError(
                        "\"" + str(arg) + "\" of type " + str(type(arg)) + " must be of type " + str(param_type) + "."
                    )
            function(*args)
        return inner
    return decorator