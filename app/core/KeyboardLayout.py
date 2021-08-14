from dataclasses import dataclass
from typing import Sequence


@dataclass
class Layout:
    name: str
    keys: Sequence[Sequence[chr]]

    def as_namespace(self) -> Sequence[int]:
        return [ord(char.upper())
                for line in self.keys
                for char in line]


QWERTY = Layout(
    name="qwerty",
    keys=[
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ]
)
