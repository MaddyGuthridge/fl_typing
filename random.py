"""
fl_typing > random

A basic recreation of some of the function contained within Python's random
module
"""

import _random
from typing import TypeVar, Sequence

T = TypeVar('T')
rng = _random.Random()


def randint(a: int, b: int) -> int:
    """Return a random number between a and b inclusive"""
    diff = abs(a - b)
    lower = min(a, b)
    return int(rng.random() * (diff + 1)) + lower


def choice(sequence: Sequence[T]) -> T:
    """Choose a random element from a sequence"""
    length = len(sequence)
    return sequence[randint(0, length-1)]


def randrange(start: int, stop: int, step: int) -> int:
    """Return a random element from a range"""
    # This is sorta inefficient, but I'm lazy
    # If it turns out to have performance issues, I'll rewrite it
    return choice(list(range(start, stop, step)))
