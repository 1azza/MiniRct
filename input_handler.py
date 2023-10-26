from enum import Enum
import pygame



class InputHandler:

  def __init__(self):
    self.held_mouse_button = False
    self.mouse_moving = False

  def handle(self, event, game) -> None:

    event_type = event.type

    if event_type == pygame.QUIT:
      pygame.quit()
      quit()

    self.handle_mouse_input(event, game)

  def handle_mouse_input(self, event, game) -> None:

    if event.type == pygame.MOUSEWHEEL:
      game.zoom(event.y)

    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button ==2:
        game.last_mouse_pos = pygame.mouse.get_pos()
        self.held_mouse_button = True
      # if game.hudmenu.menu_rect.collidepoint(pygame.mouse.get_pos()):
      #     game.hudmenu.menu_open = not game.hudmenu.menu_open
    elif event.type == pygame.MOUSEMOTION:
      if self.held_mouse_button:
        self.mouse_moving = True
        game.move_camera()
      else:
        game.select_tile()
    elif event.type == pygame.MOUSEBUTTONUP:
      if event.button == 2:
        self.held_mouse_button = False
        self.mouse_moving = False
    
