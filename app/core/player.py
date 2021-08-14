import pygame

from app.core.fs import AudioFile


class Player:

    def __init__(self) -> None:
        super().__init__()
        pygame.mixer.init()
        self._mixer = pygame.mixer

    def play(self, file: AudioFile) -> None:
        sound = self._mixer.Sound(f"{file.parent_directory}/{file.name}")
        sound.play()
