import pygame
from gameloop import GameLoop

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def setup(self):
        pygame.init()

        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Asteroids!')

        self.start()

    def start(self):        
        gameloop = GameLoop()
        gameloop.init()
        gameloop.run(self.screen, self.clock)

        pygame.quit()

        

