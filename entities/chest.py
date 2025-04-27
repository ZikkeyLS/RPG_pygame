import random
from entities.interactable_entity import *
import animation
import game_statistics

class Chest(InteractableEntity):
    def post_initialize(self):
        self.money = random.randrange(5, 10)
        self.opened = False
        
        if (game_statistics.money > 0):
            self.opened = True
            self.money = 0
        
        idle_animation_frames = self.compile_idle_animation()
        self.idleAnimation = animation.Animation(idle_animation_frames, 1 / len(idle_animation_frames))
        
        opened_animation_frames = self.compile_opened_animation()
        self.openedAnimation = animation.Animation(opened_animation_frames, 1 / len(opened_animation_frames))


    def compile_idle_animation(self):
        result_animation = []
        idle_animation_atlas = self.graphics.get_raw_image("assets/images/base_out_atlas.png")
        for i in range(1):
            result_animation.append(self.graphics.compile_atlas_image(idle_animation_atlas, 31, 31, 31, 31, 704, 544))
        return result_animation

 
    def compile_opened_animation(self):
        result_animation = []
        idle_animation_atlas = self.graphics.get_raw_image("assets/images/base_out_atlas.png")
        for i in range(1):
            result_animation.append(self.graphics.compile_atlas_image(idle_animation_atlas, 31, 31, 31, 31, 704, 576))
        return result_animation


    def on_update(self):
        if self.opened == False:
            self.idleAnimation.RunFrame(self)
        else:
            self.openedAnimation.RunFrame(self)

        if self.opened == False and abs(self.x - self.room.player.x) < 40 and abs(self.y - self.room.player.y) < 40:
            self.graphics.render_text("E", (self.x + 31 / 2 - 5, self.y - 31 / 2 - 11), False)


    def on_activate(self):
        game_statistics.money += self.money
        self.money = 0
        self.opened = True
