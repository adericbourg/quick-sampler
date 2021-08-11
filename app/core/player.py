import pygame


class Player:

    def __init__(self) -> None:
        super().__init__()
        pygame.mixer.init()

    def play(self, file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
