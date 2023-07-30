"""
FL-Python-Typing > typing

A basic stand-in for the typing module, to prevent crashes during runtime
"""

TYPE_CHECKING = False


class TypeVar:
    def __init__(self, *args, **kwargs) -> None:
        pass


class NewType:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def __call__(self, arg):
        return arg


class _AnnotationType:
    def __init__(self, name) -> None:
        self._name = name

    def __getitem__(self, key):
        return object


Any = _AnnotationType('Any')
Literal = _AnnotationType('Literal')
NoReturn = _AnnotationType('NoReturn')
Optional = _AnnotationType('Optional')
Callable = _AnnotationType('Callable')
Union = _AnnotationType('Union')
Type = _AnnotationType('Type')
Iterator = _AnnotationType('Iterator')
Generic = _AnnotationType('Generic')
Sequence = _AnnotationType('Sequence')


class Protocol:
    pass


def cast(type, val):
    return val


def overload(func):
    return func


def final(func):
    return func
