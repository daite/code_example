import pygame
import sys
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GOLD = (255, 216, 0)
SILVER = (192, 192, 192)
COPPER = (192, 112, 48)

def main():
    pygame.init()
    pygame.display.set_caption("pygame")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    tmr = 0

    while True:
        tmr += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        pygame.draw.line(screen, RED, [0, 0], [100, 200], 10)
        pygame.draw.lines(screen, BLUE, False, [[50, 300], [150, 400], [50, 500]], 10)
        pygame.draw.rect(screen, RED, [200, 50, 120, 80])
        pygame.draw.rect(screen, GREEN, [200, 200, 60, 180], 5)
        pygame.draw.polygon(screen, BLUE, [[250, 400], [200, 500], [300, 500]], 10)
        pygame.draw.circle(screen, GOLD, [400, 100], 60)
        pygame.draw.ellipse(screen, SILVER, [400-80, 300-40, 160, 80])
        pygame.draw.arc(screen, BLUE, [600-100, 300-200, 200, 400], 0, math.pi/2)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()