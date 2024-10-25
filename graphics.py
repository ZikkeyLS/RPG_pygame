import pygame
from pygame.locals import *

import tkinter
import PIL
from PIL import Image
import random
import coords
import os

class Graphics:
    def initialize(self, settings):
        pygame.init()

        self.window = pygame.display.set_mode((900, 900))
        self.window.fill((127, 127, 127))

        self.active_run = True
        self.grid_size = settings
        self.on_update_subscribers = []

        self.load_images()
        self.setup_grid()

    def update(self):
        for i in range(len(self.on_update_subscribers)):
            self.on_update_subscribers[i]()
    
    def run(self):
        while (self.active_run):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.active_run = False

            self.update()
            self.window.fill((127, 127, 127))

            for x in range(self.grid_size[0]):
                for y in range(self.grid_size[1]):
                    self.window.blit(self.background[coords.to_number([x, y], self.grid_size[0])][1], [x * 35, y * 35])
                    self.window.blit(self.grid[coords.to_number([x, y], self.grid_size[0])][1], [x * 35, y * 35])

            #pygame.display.update()
            pygame.display.flip()

    def native_image_to_pygame(self, current_image):
        return pygame.image.fromstring(current_image.tobytes(), current_image.size, current_image.mode)

    def load_images(self):
        atlas_env1 = Image.open("assets/images/base_out_atlas.png")
        main_hero_atlas_idle = Image.open("assets/images/Warrior_1/Idle.png")

        self.images = {}

        self.images["Empty"] = self.native_image_to_pygame(Image.new("RGBA", (35, 35), (255, 255, 255, 255)))
        self.images["WarriorIdle"] = self.native_image_to_pygame(main_hero_atlas_idle.crop([30, 50, 30+37, 50+45]).resize([30, 35]))

    def setup_grid(self):
        self.grid = []
        self.background = []
        self.cell_size = 35

        for x in range(self.grid_size[0]):
            for y in range(self.grid_size[1]):
                color = "#%06x" % random.randint(0, 0xFFFFFF)
                cell = self.images["WarriorIdle"]
                back = self.images["Empty"]

                self.background.append([coords.to_number([x, y], self.grid_size[0]), back, color])
                self.grid.append([coords.to_number([x, y], self.grid_size[0]), cell, color])

    def get_cell(self, position):
        for i in range(len(self.grid)):
            if self.grid[i][0] == position:
                return self.grid[i]
