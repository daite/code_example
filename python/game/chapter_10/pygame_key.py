import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    pygame.init()
    pygame.display.set_caption("pygame")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()
        txt1 = font.render("UP" + str(key[pygame.K_UP]) + " DOWN" + str(key[pygame.K_DOWN]), True, WHITE, GREEN)
        txt2 = font.render("LEFT" + str(key[pygame.K_LEFT]) + " RIGHT" + str(key[pygame.K_RIGHT]), True, WHITE, BLUE)
        txt3 = font.render("SPACE" + str(key[pygame.K_SPACE]) + " ENTER" + str(key[pygame.K_RETURN]), True, WHITE, RED)
        screen.fill(BLACK)
        screen.blit(txt1, [0, 0])
        screen.blit(txt2, [0, 100])
        screen.blit(txt3, [0, 200])
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()