import pygame
from pygame.locals import *

keys_down = []
keys_up = []

def is_pressed(key_id):
    keys = pygame.key.get_pressed()
    return keys[key_id] != 0

def is_down(key_id):
    return key_id in keys_down

def is_up(key_id):
    return key_id in keys_up
