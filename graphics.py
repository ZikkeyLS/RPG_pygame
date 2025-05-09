import pygame
import button
from pygame.locals import *
from PIL import Image
import coords
import input_bindings
import random
import game_statistics
import settings

class Graphics:
    def initialize(self, settings):
        pygame.init()
        pygame.font.init()
        
        self.window = pygame.display.set_mode((900, 900))
        self.window.fill((127, 127, 127))
        
        self.main_menu_opened = True
        
        self.ui_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.ui_texts = {}
        self.game_font = pygame.font.SysFont('Comic Sans MS', 22)
        self.game_texts = {}

        gameText = ""
        if game_statistics.save_exists():
            gameText = "Продолжить"
        else:
            gameText = "Начать игру"
        self.start_button = button.Button(300, 350, 350, 150, self.ui_font, self.window, gameText, self.run_game)
        
        self.close_game_button = button.Button(650, 800, 225, 75, self.ui_font, self.window, "Выйти из игры", self.stop_game)
        
        self.cell_size = 31

        self.active_run = True
        self.grid_size = settings
        self.on_update_subscribers = []

        self.load_images()
        self.setup_grid()
    

    def render_text(self, initial_message, initial_position, is_ui = True, color = (0, 0, 0)):
        if is_ui:        
            text = self.ui_font.render(initial_message, False, color)
            self.ui_texts[text] = initial_position
        else:
            text = self.game_font.render(initial_message, False, color)
            self.game_texts[text] = initial_position


    def run_game(self):
        self.main_menu_opened = False
        game_statistics.try_load_save()
        self.world.initialize(settings.GRID_SIZE, self)
        self.on_update_subscribers.append(self.world.on_update)

        
    def stop_game(self):
        if self.main_menu_opened == False:
            game_statistics.save()
        self.active_run = False


    def update(self):
        if game_statistics.killed > 0 and game_statistics.money > 0:
            self.render_text("Вы прошли игру!", [350, 125], True, (0, 255, 0))
        
        for i in range(len(self.on_update_subscribers)):
            self.on_update_subscribers[i]()


    def run(self):
        while (self.active_run):
            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    self.stop_game()
                if event.type == pygame.KEYDOWN:
                    input_bindings.keys_down.append(event.key)
                if event.type == pygame.KEYUP:
                    input_bindings.keys_up.append(event.key) 

            self.window.fill((127, 127, 127))
            self.update()

            if self.world.initialized:   
                for x in range(self.grid_size[0]):
                    for y in range(self.grid_size[1]):
                        self.window.blit(self.background[coords.to_number([x, y], self.grid_size[0])][1], [x * self.cell_size, y * self.cell_size])
                        
                for entity in self.world.current_room.entities:
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
                
            if (self.main_menu_opened):
                self.start_button.process()
        
            self.close_game_button.process()

            pygame.display.flip()
            
            input_bindings.keys_down = []
            input_bindings.keys_up = []


    def native_image_to_pygame(self, current_image):
        return pygame.image.fromstring(current_image.tobytes(), current_image.size, current_image.mode)


    def load_images(self):        
        self.atlas_env1 = Image.open("assets/images/base_out_atlas.png")
        
        self.images = {}
        self.images["Empty"] = self.native_image_to_pygame(Image.new("RGBA", (self.cell_size, self.cell_size), (255, 255, 255, 255)))
        self.images["Transparent"] = self.native_image_to_pygame(Image.new("RGBA", (self.cell_size, self.cell_size), (255, 255, 255, 0)))
        self.images["Tree"] = self.native_image_to_pygame(self.atlas_env1.crop([768, 485, 768+85, 485+90]))
        self.images["Pond"] = self.native_image_to_pygame(self.atlas_env1.crop([672, 417, 672+95, 417+95]))

        self.grass_variants = []
        for i in range(3):
            self.grass_variants.append(self.native_image_to_pygame(self.atlas_env1.crop([672+self.cell_size*i, 160, 672+self.cell_size+self.cell_size*i, 160+self.cell_size])))

 
    def get_raw_image(self, imagePath):
        return Image.open(imagePath)


    def compile_atlas_image(self, atlas, resultSizeX, resultSizeY, cropX, cropY, cropPosX, cropPosY):
        return self.native_image_to_pygame(atlas.crop([cropPosX, cropPosY, cropPosX+cropX, cropPosY+cropY]).resize([resultSizeX, resultSizeY]))


    def setup_grid(self):
        self.grid = {}
        self.background = []
        random.seed(123321)
 
        for x in range(self.grid_size[0]):
            for y in range(self.grid_size[1]):
                self.background.append([coords.to_number([x, y], self.grid_size[0]), self.grass_variants[random.randrange(0, len(self.grass_variants))]])


    def get_cell(self, position):
        for i in range(len(self.grid)):
            if self.grid[i][0] == position:
                return self.grid[i]
