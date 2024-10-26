import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT   

class GameLoop():
    def init(self):
        self.create_groups()
        self.set_containers()
        self.dt = 0

    def create_groups(self):
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

    def set_containers(self):
        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.updatable)
        Shot.containers = (self.shots, self.updatable, self.drawable)

    def run(self, screen, clock):
        asteroid_field = AsteroidField()
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  
        is_game_on = True
        while is_game_on:
            screen.fill("black")
            self.proccess_input()

            should_continue = self.update(screen)
            if not should_continue:
                is_game_on = False

            self.render(clock)
        
        print("Game over!")
        print(f"Your score was: {self.player.get_score()}")
    
    def is_game_over(self, asteroid, player):
        return asteroid.collition(player)
    
    def proccess_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def update(self, screen):
        for item in self.drawable:
            item.draw(screen)
            
        for item in self.updatable:
            item.update(self.dt)

        for asteroid in self.asteroids:
            for shot in self.shots:
                if asteroid.collition(shot):
                    asteroid.split()
                    shot.kill()
                    self.player.increase_score()

                if self.is_game_over(asteroid, self.player):
                    return False
                
        return True
                
    def render(self, clock):
        pygame.display.flip()
        last_time = clock.tick(60)
        self.dt = last_time / 1000