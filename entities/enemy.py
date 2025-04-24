import random
from entities.interactable_entity import *
import animation
import game_statistics

class Enemy(Entity):
    def post_initialize(self):
        self.hp = 5
        
        idle_animation_frames = self.compile_idle_animation()
        self.idleAnimation = animation.Animation(idle_animation_frames, 1 / len(idle_animation_frames))
        

    def compile_idle_animation(self):
        result_animation = []
        idle_animation_atlas = self.graphics.get_raw_image("assets/images/Warrior_1/Idle.png")
        for i in range(6):
            result_animation.append(self.graphics.compile_atlas_image(idle_animation_atlas, 30, 35, 37, 48, 29 + (i * 96), 48))
        return result_animation


    def on_update(self):
        self.idleAnimation.RunFrame(self)
        self.graphics.render_text(str(self.hp) + " хп", (self.x + 31 / 2 - 14, self.y - 31 / 2 - 8), False)

    def kill(self):
        self.room.entities.remove(self)

        
    def give_damage(self, amount):
        amount = abs(amount)
        self.hp -= amount
        if (self.hp <= 0):
            self.kill()
            game_statistics.killed += 1
