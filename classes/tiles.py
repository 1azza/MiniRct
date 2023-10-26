import pygame
PATH = 'assets'
def load(flname):
    return pygame.image.load(f'{PATH}/{flname}').convert_alpha()
class Tiles:
    def __init__(self):
        self.blocks = Blocks()
        self.layers = Layers()

class Blocks:
    def __init__(self):
        self.grass = load("grass_block.png")
        self.path = load("path_block.png")


class Layers:
    def __init__(self):
        self.grass = load("grass.png")
        self.path = load("path.png")
        self.selected = load("grass_selected.png")
