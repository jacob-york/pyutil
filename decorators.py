"""Practical Use Decorators (and decorator factories)"""
from types import UnionType
from datetime import datetime
from typing import Callable, get_type_hints


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
                function(*args, **kwargs)
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
            function(*args, **kwargs)
        except Exception:
            pass

    return inner


# TODO: @statictyping which detects the type hints in parameters and raises a TypeError if they don't agree
def expects(*types: type | tuple[type[int], type[float]] | UnionType,
            method: bool = False):
    """A stricter alternative to type hinting.
    Unlike type hinting, this will actually raise a TypeError if your params aren't of the right type.
    Example usages:


    @expects(int)
    def my_func(param1):
        pass


    # kw arg here makes no difference
    @expects(dict, str, method=False)
    def my_func(param1, param2):
        pass


    class A:

        @expects(int, str, bool, method=True)
        def my_method(self, param1, param2, param3):
            pass

    """

    def decorator(function):
        def method_inner(self, *args):
            for arg, type_ in zip(args, types):
                if not isinstance(arg, type_):
                    raise TypeError(f'"{arg}" of type {type(arg)} must be of type {type_}.')
            function(self, *args)

        def function_inner(*args):
            for arg, type_ in zip(args, types):
                if not isinstance(arg, type_):
                    raise TypeError(f'"{arg}" of type {type(arg)} must be of type {type_}.')
            function(*args)

        return method_inner if method else function_inner

    return decorator


def enforce_type_hints(function):
    """Wil enforce your type hints by raising a TypeError if an argument doesn't match."""
    # TODO: clean-up
    # TODO: only works if every param is type-hinted
    def inner(*args, **kwargs):
        type_hints = get_type_hints(function)
        common_keys = set(kwargs.keys()).intersection(set(type_hints.keys()))

        for arg, type_ in zip(args, type_hints.values()):
            if not isinstance(arg, type_):
                raise TypeError(f'"{arg}" of type {type(arg)} must be of type {type_}.')

        for param, kwarg, type_ in ((param, kwargs[param], type_hints[param]) for param in common_keys):
            if not isinstance(kwarg, type_):
                raise TypeError(f'"{param}" must be {type_} (passed: {type(kwarg)} ).')

        function(*args, **kwargs)
    return inner


def main():
    """For use in Testing and Debugging."""
    pass


if __name__ == "__main__":
    main()
