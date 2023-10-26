from classes.map import Map
import pygame
from renderer import IsometricRenderer, MenuRenderer
from input_handler import InputHandler
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.map = Map()
        self.iso_renderer = IsometricRenderer(self.screen, pygame.font.Font(None, 48), self.map)
        self.clock = pygame.time.Clock()
        self.hudmenu = MenuRenderer(self.screen, pygame.font.Font(None, 16))
        self.event_handler = InputHandler()
        self.running = True
        self.held_mb4 = False
        
    def run(self):
        self.iso_renderer.load_map()
        self.tile_coords = (0, 0)
        while True:
            self.update()

    def update(self):
        self.clock.tick(144)
        events = pygame.event.get()
        for event in events:
            operation = self.event_handler.handle(event, self)
            if operation == 0:
                return 0
            self.hudmenu.update(event)
        pygame.display.flip()
        
    def move_camera(self):
        self.iso_renderer.offset_x += pygame.mouse.get_pos()[0] - self.last_mouse_pos[0]
        self.iso_renderer.offset_y += pygame.mouse.get_pos()[1]- self.last_mouse_pos[1] 
        self.last_mouse_pos = pygame.mouse.get_pos()
        self.iso_renderer.load_map()
        return 1
        
    def select_tile(self):
        map_pos = self.map.get_position(pygame.mouse.get_pos(), self.iso_renderer.tile, self.iso_renderer.offset_x, self.iso_renderer.offset_y)
        self.iso_renderer.render_tile_selector(map_pos)
        return 1
        
    def zoom(self, y):
        self.iso_renderer.zoom(y)
        return 1
        



if __name__ == "__main__":
    game = Game()
    game.run()
