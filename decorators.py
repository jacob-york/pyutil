"""Practical Use Decorators (and decorator factories)"""
from types import UnionType


def log_error(file_name: str = "error_log"):
    """Decorator factory.
    logs all Exceptions during function into a file called error_log.txt.
    """
    from datetime import datetime

    def decorator(function):
        def inner(*args, **kwargs):
            try:
                function(*args, **kwargs)
            except Exception as e:
                with open(f"{file_name}.txt", "a") as error_file:
                    error_file.write(f"{datetime.now()} {type(e)}: {e}\n")
        return inner
    return decorator


def ignore_if_error(function):
    """Skips the function if there is any error."""
    def inner(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception:
            pass
    return inner


def expects(*types: type | tuple[type[int], type[float]] | UnionType,
            method: bool = False):
    """ A stricter alternative to type hinting.
    Unlike type hinting, this will actually raise a TypeError if your params aren't of the right type.
    Example usages:

    @expects(int)
    def my_func(param1):
        code...

    @expects(dict, str)
    def my_func(param1, param2):
        code...

    @expects(int, str, bool, method=True)
    def my_method(self, param1, param2, param3):
        code....
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


def main():
    """For use in Testing and Debugging."""
    pass


if __name__ == "__main__":
    main()
