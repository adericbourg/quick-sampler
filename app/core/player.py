import pygame


class Player:

    def __init__(self) -> None:
        super().__init__()
        pygame.mixer.init()
        self._mixer = pygame.mixer

    def play(self, file):
        sound = self._mixer.Sound(file)
        sound.play()
