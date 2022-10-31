import inspect
from pyclbr import Function
from pydoc import locate
from inspect import ArgSpec


def f(x: int, y: float, z):
    return x + y + z


def safe_call(f: Function, **kwargs):
    """
    This function gets a function and arguments, checks whether all the arguments are of the right type and prints
    the values if they are.
    """
    lst = inspect.getfullargspec(f).annotations
    for arg, val in kwargs.items():
        if arg in lst:
            s = lst.get(arg)
            if s != type(val):
                raise Exception("value types mismatch")
    print(f(**kwargs))


if __name__ == '__main__':
    safe_call(f, x=5, y=7.0, z=3)
    safe_call(f, x=5, y="abc", z=3)

