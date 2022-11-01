import inspect
from pyclbr import Function


def f(x: int, y: float, z):
    return x + y + z


def safe_call(f: Function, *args, **kwargs):
    """
    This function gets a function and arguments, checks whether all the arguments are of the right type and prints
    the values if they are.

    >>> safe_call(f, 5, 7.0, 3)
    15.0

    >>> safe_call(f, 5, 7, 3)
    Traceback (most recent call last):
        ...
    Exception: value types mismatch

    >>> safe_call(f, x=5, y="abc", z=3)
    Traceback (most recent call last):
        ...
    Exception: value types mismatch

    >>> safe_call(f, 5, "abc", 3)
    Traceback (most recent call last):
        ...
    Exception: value types mismatch

    """
    lst = inspect.getfullargspec(f).annotations
    for arg, val in kwargs.items():
        if arg in lst:
            s = lst.get(arg)
            if s != type(val):
                raise Exception("value types mismatch")
    i = 0
    for item in lst.values():
        type_args = args[i]
        i += 1
        if item != type(type_args):
            raise Exception("value types mismatch")

    print(f(*args, **kwargs))


if __name__ == '__main__':
    safe_call(f, x=5, y=7.0, z=3)

