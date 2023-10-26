import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drop Down Menu")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

font = pygame.font.SysFont(None, 48)

menu_caption = font.render("Menu", True, WHITE)
menu_surface = pygame.Surface((100, 50))
menu_surface.fill(GRAY)
menu_rect = menu_surface.get_rect(bottomleft=(10, SCREEN_HEIGHT-10))

menu_open = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_rect.collidepoint(pygame.mouse.get_pos()):
                menu_open = not menu_open


    if menu_open:
        pygame.draw.rect(screen, WHITE, menu_rect)
        screen.blit(menu_caption, (menu_rect.x+10, menu_rect.y+10))

    else:
        screen.blit(menu_surface, menu_rect)
        screen.blit(menu_caption, (menu_rect.x+10, menu_rect.y+10))

    pygame.display.update()
