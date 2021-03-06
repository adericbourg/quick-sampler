from dataclasses import dataclass
from typing import Sequence


@dataclass
class Layout:
    name: str
    keys: Sequence[Sequence[chr]]

    def as_namespace(self) -> Sequence[int]:
        return [char
                for line in self.keys
                for char in line]


QWERTY = Layout(
    name="qwerty",
    keys=[
        ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\''],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
    ]
)
