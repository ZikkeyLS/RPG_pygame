import pygame
from pygame.locals import *

def is_pressed(key_id):
    keys = pygame.key.get_pressed()
    return keys[key_id] != 0
