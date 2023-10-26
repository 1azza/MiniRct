import math


def iso_to_cart(coords, tilw, tilh):
    x = coords[0]*2
    y = coords[1]*4
    # Get projected axes
    x_axis = (tilw / 2, tilh / 2)
    y_axis = (-tilw / 2, tilh / 2)

    # Project point onto each axis
    proj_x = x * (x_axis[0] / tilw) + \
        y * (x_axis[1] / tilh)
    proj_y = x * (y_axis[0] / tilw) + \
        y * (y_axis[1] / tilh)

    # Round projected values
    proj_x = math.floor(proj_x / tilw)
    proj_y = math.ceil(proj_y / tilh)
    return proj_x, proj_y

class Map:
    def __init__(self) -> None:
        with open('data/map.txt', 'r') as f:
            lines = f.readlines()

        self.map_data = []
        for line in lines:
            self.map_data.append([char for char in line.strip()])

    def get_map_tile_from_coords(self, coords):
        return self.map_data[coords[1]][coords[0]]

    def update_map(self, coords, tile):
        self.map_data[coords[1]][coords[0]] = tile

    def get_position(self, coords, tilw,offset_x, offset_y):
        coords = iso_to_cart([coords[0]-3-offset_x,coords[1]-10-offset_y], tilw, tilw)
        try:
            if self.map_data[coords[1]][coords[0]] == ' ' or coords[0] < 0 or coords[1] < 0:
                return None
        except IndexError:
            return None
        return coords

