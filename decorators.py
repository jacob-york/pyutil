"""Practical Use Decorators (and decorator factories)"""

import inspect
from datetime import datetime
from typing import Callable


def log_error(str_function: str | Callable):
    """Logs all Exceptions during function into a txt file before closing.
    The name of the txt file is customizable. Syntax is as shown:

    # logs errors into file named "error_log":
    @log_error
    def main():
        pass

    # logs errors into file "my_errors.txt":
    @log_error("my_errors")
    def main():
        pass

    Passing "error_log" will be identical to no arguments.
    """
    if isinstance(str_function, Callable):
        file_name = "error_log"
        passed_function = True
    else:
        file_name = str_function
        passed_function = False

    def decorator(function):
        def inner(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except Exception as e:
                print(e)
                with open(f"{file_name}.txt", "a") as error_file:
                    error_file.write(f"{datetime.now()} {type(e)}: {e}\n")

        return inner

    # log_error toggles between being a decorator factory or a normal decorator
    # based on its parameters.
    return decorator(str_function) if passed_function else decorator


def ignore_if_error(function):
    """Skips the function if there is any error."""
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception:
            pass

    return inner


def enforce_type_hints(function):
    """Raises a TypeError if the decorated function's type hints (on parameters)
    don't agree with the arguments passed.
    """
    def inner(*args, **kwargs):
        annotations = function.__annotations__
        arguments = inspect.signature(function).bind(*args, **kwargs).arguments
        unchecked = set(annotations.keys()).intersection(set(arguments.keys()))

        for param_name, arg, type_ in ((param, arguments[param], annotations[param]) for param in unchecked):
            if not isinstance(arg, type_):
                raise TypeError(f'"{param_name}" requires {type_} (passed: {type(arg)} ).')

        return function(*args, **kwargs)
    return inner


def main():
    """For use in Testing and Debugging."""
    pass


if __name__ == "__main__":
    main()
