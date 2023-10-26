import json
import pygame
def load_asset(file, path='assets'):
    asset = pygame.image.load(f'{path}/{file}').convert_alpha()
        
    return asset


def get_asset_data():
    with open('data/assets_map.json', 'r') as f:
        data = json.load(f)
    return data