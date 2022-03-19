"""
FL-Python-Typing > typing_extensions

A basic stand-in for the typing module, to prevent crashes during runtime
"""

class _AnnotationType:
    def __init__(self, name) -> None:
        self._name = name
    def __getitem__(self, key):
        return object

TypeGuard = _AnnotationType('TypeGuard')
Concatenate = _AnnotationType('Concatenate')
Self = _AnnotationType('Self')

class ParamSpec:
    def __init__(self, *args, **kwargs) -> None:
        self.args = ()
        self.kwargs = ()
