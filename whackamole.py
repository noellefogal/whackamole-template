import pygame
import random

def reset_screen(screen):
    screen.fill("light green")
    i = 32
    while i < 640:
        pygame.draw.line(screen, "dark blue", (i, 0), (i, 512))
        i += 32
    i = 32
    while i < 512:
        pygame.draw.line(screen, "dark blue", (0, i), (640, i))
        i += 32

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        reset_screen(screen)
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        mole_coor = (0, 0)
        while running:
            pygame.display.flip()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col = x-x%32
                    row = y-y%32
                    if (col,row) == mole_coor:
                        reset_screen(screen)
                        random_x = random.randrange(0, 640)
                        random_y = random.randrange(0, 512)
                        screen.blit(mole_image, mole_image.get_rect(topleft=((random_x - random_x%32), random_y - random_y%32)))
                        mole_coor = ((random_x - random_x%32),(random_y - random_y%32))
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
