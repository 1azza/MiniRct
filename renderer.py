import pygame
from classes.tiles import Tiles

class Renderer:
    def __init__(self, screen, font) -> None:
        self.screen = screen
        self.font = font


class IsometricRenderer(Renderer):
    def __init__(self, screen, font, map) -> None:
        super().__init__(screen, font)
        self.tiles = Tiles()
        self.map = map
        self.selected_tile = None
        self.tile = 32  # holds the tile width and height
        self.offset_x = screen.get_width() / 2
        self.offset_y = screen.get_height() / 2
    def load_map(self):
        self.screen.fill((100, 100, 100))
        for row_nb, row in enumerate(self.map.map_data):
            for col_nb, tile in enumerate(row):
                tile_img = self.tiles.blocks.grass
                self.render_tile((col_nb, row_nb), tile_img)
        pygame.display.flip()

    def render_tile(self, coords: tuple, tile):
        if coords == None:
            return
        tile = pygame.transform.scale(tile, (self.tile, self.tile))
        half_tile = self.tile/2
        cart_x = coords[0] * half_tile
        cart_y = coords[1] * half_tile

        iso_x = (cart_x - cart_y)
        iso_y = (cart_x + cart_y)/2
        self.screen.blit(tile, (iso_x+self.offset_x, iso_y+self.offset_y))
        return coords

    def render_tile_selector(self, coords):
        if self.selected_tile == None:
            self.selected_tile = coords

        if coords == self.selected_tile:
            self.render_tile(coords, self.tiles.layers.selected)
            self.selected_tile = coords

        else:
            tile = self.tiles.layers.grass
            self.render_tile(self.selected_tile, tile)
            self.selected_tile = coords
            
            
    def zoom(self, y):
        if y >= 0 and self.tile <= 64:
            self.tile +=4
        elif self.tile > 0:
            self.tile -=4
        self.load_map()


class Button():
    def __init__(self, screen, text, function, x, y, width, height, color, hover_color, font, font_color, outline=None, outline_color=None, outline_thickness=1):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.font_size = font
        self.font_color = font_color
        self.outline = outline
        self.clicked = False
        self.hover_color = hover_color
        self.function = function
        self.outline_color = outline_color 
        self.color = color
        self.outline_thickness = outline_thickness

        pygame.draw.rect(screen, color, (x, y, width, height))
        if outline:
            pygame.draw.rect(screen, outline_color,
                                (x, y, width, height), outline_thickness)
        self.text = font.render(text, True, font_color)

    def update(self, event):
        mouse = pygame.mouse.get_pos()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(self.screen, self.hover_color,
                             (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.screen, (100, 100, 100, 100),
                             (self.x, self.y, self.width, self.height))
        self.screen.blit(self.text, (self.x + (self.width/2 - self.text.get_width()/2),
                                     self.y + (self.height/2 - self.text.get_height()/2)))

    def clear(self, event):
        pygame.draw.rect(self.screen, (100,100,100,100),
                         (self.x, self.y, self.width, self.height))
        if self.outline:
            pygame.draw.rect(self.screen, (100, 100, 100, 100),
                             (self.x, self.y, self.width, self.height), self.outline_thickness)

class Dropdown(Button):
    def __init__(self, screen, text, function, x, y, width, height, color, hover_color, font, font_color, outline=None, outline_color=None, outline_thickness=1):
        super().__init__(screen, text, function, x, y, width, height, color, hover_color,
                         font, font_color, outline=None, outline_color=None, outline_thickness=1)
        self.items = []
    def add_button(self, text, function):

        button = Button(self.screen, text, function, self.x+(50*(len(self.items)+1)), self.y, self.width, self.height, self.color, self.hover_color, self.font, self.font_color, self.outline, self.outline_color, self.outline_thickness)
        self.items.append(button)

     
    def update(self, event):

        mouse = pygame.mouse.get_pos()

        if self.clicked:
            # Draw extra buttons if clicked
            for item in self.items:
                item.update(event)
        else:
            for item in self.items:
                item.clear(event)
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(self.screen, self.hover_color,
                            (self.x, self.y, self.width, self.height))

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                self.clicked = not self.clicked

                if self.clicked:
                    print("Toggle ON")
                else:
                    print("Toggle OFF")

        else:
            pygame.draw.rect(self.screen, (100, 100, 100, 100),
                             (self.x, self.y, self.width, self.height))
        self.screen.blit(self.text, (self.x + (self.width/2 - self.text.get_width()/2),
                        self.y + (self.height/2 - self.text.get_height()/2)))
        
class MenuRenderer(Renderer):

    def __init__(self, screen, font) -> None:
        super().__init__(screen, font)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (150, 150, 150)
        self.menu_open = False
        self.path_dropdown = Dropdown(self.screen, "utilities", self.test, 0,
                                       0, 50, 50, self.GRAY, self.WHITE, self.font, self.BLACK, True, self.BLACK, 1)
        self.path_dropdown.add_button("paths", self.test)
        self.path_dropdown.add_button("benches", self.test)
        self.path_dropdown.add_button("bins", self.test)
    def test(self, event):
        print("test")
    # def dropdown(self,event):
    #     self.add_button(event, "Menu", self.test, 0, 0, 100, 50, self.GRAY,
    #                     self.WHITE, self.font, self.BLACK, True, self.BLACK, 1)

        
    def update(self, event):
        print(event)
        self.path_dropdown.update(event)


        pygame.display.update()
