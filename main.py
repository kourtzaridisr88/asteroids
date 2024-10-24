import pygame
from constants import *
from player import Player


def main():
    pygame.init()


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)   
    while True:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return
 
        
        screen.fill("black")
        
        player.draw(screen)
        pygame.display.flip()
        last_time = clock.tick(60)
        dt = last_time / 1000

        # render player


if __name__ == "__main__":
   main()
