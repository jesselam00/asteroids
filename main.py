import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # print("Starting Asteroids!")
    # print("Screen width:", constants.SCREEN_WIDTH)
    # print("Screen height:", constants.SCREEN_HEIGHT)
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()

if __name__ == "__main__":
    main()
