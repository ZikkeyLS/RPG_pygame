import pygame
from pygame.locals import *
import PIL
from PIL import Image
import random
import coords
import input_bindings

class Graphics:
    def initialize(self, settings):
        pygame.init()
        pygame.font.init()
        
        self.ui_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.ui_texts = {}
        self.game_font = pygame.font.SysFont('Comic Sans MS', 16)
        self.game_texts = {}

        self.window = pygame.display.set_mode((900, 900))
        self.window.fill((127, 127, 127))

        self.active_run = True
        self.grid_size = settings
        self.on_update_subscribers = []

        self.load_images()
        self.setup_grid()

    def render_text(self, initial_message, initial_position, is_ui = True):
        if is_ui:        
            text = self.ui_font.render(initial_message, False, (0, 0, 0))
            self.ui_texts[text] = initial_position
        else:
            text = self.game_font.render(initial_message, False, (0, 0, 0))
            self.game_texts[text] = initial_position

    def update(self):
        for i in range(len(self.on_update_subscribers)):
            self.on_update_subscribers[i]()
    
    def run(self):
        while (self.active_run):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.active_run = False
                if event.type == pygame.KEYDOWN:
                    input_bindings.keys_down.append(event.key)
                if event.type == pygame.KEYUP:
                    input_bindings.keys_up.append(event.key) 

            self.update()
            self.window.fill((127, 127, 127))

            for x in range(self.grid_size[0]):
                for y in range(self.grid_size[1]):
                    self.window.blit(self.background[coords.to_number([x, y], self.grid_size[0])][1], [x * 35, y * 35])

            for entity in self.world.currentRoom.entities:
                if (entity.image == None):
                    continue
                entity_image = entity.image.copy()
                x_flip = entity.size_x < 0
                y_flip = entity.size_y < 0
                if x_flip or y_flip:
                    entity_image = pygame.transform.flip(entity_image, x_flip, y_flip) 
                self.window.blit(entity_image, [entity.x, entity.y])
        
            for text, position in self.game_texts.items():
                self.window.blit(text, position)
            self.game_texts.clear()
            
            for text, position in self.ui_texts.items():
                self.window.blit(text, position)
            self.ui_texts.clear()

            pygame.display.flip()
            
            input_bindings.keys_down = []
            input_bindings.keys_up = []

    def native_image_to_pygame(self, current_image):
        return pygame.image.fromstring(current_image.tobytes(), current_image.size, current_image.mode)

    def load_images(self):
        atlas_env1 = Image.open("assets/images/base_out_atlas.png")
        main_hero_atlas_idle = Image.open("assets/images/Warrior_1/Idle.png")

        self.images = {}

        self.images["Empty"] = self.native_image_to_pygame(Image.new("RGBA", (35, 35), (255, 255, 255, 255)))
        self.images["Transparent"] = self.native_image_to_pygame(Image.new("RGBA", (35, 35), (255, 255, 255, 0)))
        self.images["WarriorIdle"] = self.native_image_to_pygame(main_hero_atlas_idle.crop([30, 50, 30+37, 50+45]).resize([30, 35]))

    def get_raw_image(self, imagePath):
        return Image.open(imagePath)

    def compile_atlas_image(self, atlas, resultSizeX, resultSizeY, cropX, cropY, cropPosX, cropPosY):
        return self.native_image_to_pygame(atlas.crop([cropPosX, cropPosY, cropPosX+cropX, cropPosY+cropY]).resize([resultSizeX, resultSizeY]))

    def setup_grid(self):
        self.grid = {}
        self.background = []
        self.cell_size = 35

        for x in range(self.grid_size[0]):
            for y in range(self.grid_size[1]):
                color = "#%06x" % random.randint(0, 0xFFFFFF)
                cell = self.images["WarriorIdle"]
                back = self.images["Empty"]
                transparent = self.images["Transparent"]

                self.background.append([coords.to_number([x, y], self.grid_size[0]), back, color])
                #self.grid.append([coords.to_number([x, y], self.grid_size[0]), [x, y * 35], transparent, color])

    def get_cell(self, position):
        for i in range(len(self.grid)):
            if self.grid[i][0] == position:
                return self.grid[i]
