import glob
import os
from typing import Sequence
from dataclasses import dataclass
from pathlib import Path


@dataclass
class AudioFile:
    name: str
    parent_directory: str
    relative_parent_directory: str


def list_files(directory) -> Sequence[AudioFile]:
    if not os.path.isdir(directory):
        return []
    audio_files = []
    for audio_file in glob.iglob(directory + "/**/*.wav", recursive=True):
        path = Path(audio_file)
        audio_files.append(
            AudioFile(
                path.name,
                str(path.parent),
                str(path.parent).replace(directory, "")
            )
        )
    return audio_files
