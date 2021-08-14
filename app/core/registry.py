from dataclasses import dataclass
from typing import Sequence, Optional, Dict

from app.core.fs import AudioFile


@dataclass
class FileMapping:
    file: AudioFile
    key: chr


__registry: Dict[int, AudioFile] = dict()


def register(files: Sequence[AudioFile], namespace: Sequence[chr]) -> Sequence[FileMapping]:
    if len(namespace) < len(files):
        print("WARNING: namespace smaller than files to map")
    for file, code in zip(files, namespace):
        if file is None or code is None:
            break
        __registry[code] = file
    return [FileMapping(file=file, key=code) for (code, file) in __registry.items()]


def get(key: chr) -> Optional[AudioFile]:
    if key in __registry:
        return __registry[key]
    return None
