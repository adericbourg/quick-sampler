from typing import Sequence, TypedDict, Dict

from app.core.fs import AudioFile
from dataclasses import dataclass

# a-z + 0-9
ASCII_CODES = list(range(65, 90 + 1)) + list(range(48, 57 + 1))


@dataclass
class FileMapping:
    file: AudioFile
    key: str


__registry: Dict[int, AudioFile] = dict()


def register(files: Sequence[AudioFile]) -> Sequence[FileMapping]:
    for file, ascii_code in zip(files, ASCII_CODES):
        if file is None or ascii_code is None:
            break
        __registry[ascii_code] = file
    return [FileMapping(file=file, key=ascii_code) for (ascii_code, file) in __registry.items()]
