import random
from entities.interactable_entity import *
import animation
import game_statistics

class Chest(InteractableEntity):
    def post_initialize(self):
        self.money = random.randrange(5, 10)
        
        idle_animation_frames = self.compile_idle_animation()
        self.idleAnimation = animation.Animation(idle_animation_frames, 1 / len(idle_animation_frames))
    
    def compile_idle_animation(self):
        result_animation = []
        idle_animation_atlas = self.graphics.get_raw_image("assets/images/base_out_atlas.png")
        for i in range(1):
            result_animation.append(self.graphics.compile_atlas_image(idle_animation_atlas, 31, 31, 31, 31, 704, 544))
        return result_animation
    
    def on_update(self):
        self.idleAnimation.RunFrame(self)
    
    def on_activate(self):
        game_statistics.money += self.money
        self.money = 0
