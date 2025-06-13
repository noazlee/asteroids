import pygame
from constants import *
from player import Player

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

    # Game loop: check player input, update game world, draw game to screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
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