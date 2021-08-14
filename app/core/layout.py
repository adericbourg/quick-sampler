from dataclasses import dataclass
from typing import Sequence


@dataclass
class Layout:
    name: str
    keys: Sequence[Sequence[str]]


QWERTY = Layout(
    name="qwerty",
    keys=[
        ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
        ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
        ["z", "x", "c", "v", "b", "n", "m"]
    ]
)
