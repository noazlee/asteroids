import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    field = AsteroidField()

    # Game loop: check player input, update game world, draw game to screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                return

            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()

        # Fill screen with black
        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        # Update screen
        pygame.display.flip()
        # Framerate = 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()