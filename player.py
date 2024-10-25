import entity
from input_bindings import *
import input_bindings
import animation

class Player(entity.Entity):
    def __init__(self):
        self.moveFrames = 8
        self.result_scalar = [0, 0]
        self.idleAnimation = animation.Animation(self.compile_idle_animation(), self.room)

    def compile_idle_animation():
        result_animation = []
        # add frames from grpahics compile_atlas_image in graphics
        return result_animation

    def on_update(self):
        if is_pressed(K_LEFT):
            self.result_scalar[0] -= 1
        elif is_pressed(K_RIGHT):
            self.result_scalar[0] += 1
        if is_pressed(K_UP):
            self.result_scalar[1] -= 1
        elif is_pressed(K_DOWN):
            self.result_scalar[1] += 1

        normalized = [round(self.result_scalar[0] / max(abs(self.result_scalar[0]), 0.1)), round(self.result_scalar[1] / max(abs(self.result_scalar[1]), 0.1))]
        if abs(self.result_scalar[0]) >= self.moveFrames and abs(self.result_scalar[1]) > self.moveFrames:
            self.room.move_entity(self, self.x + normalized[0], self.y + normalized[1])
            self.result_scalar = [0, 0]
        elif abs(self.result_scalar[0]) >= self.moveFrames:
            self.room.move_entity(self, self.x + normalized[0], self.y)
            self.result_scalar[0] = 0
        elif abs(self.result_scalar[1]) >= self.moveFrames:
            self.room.move_entity(self, self.x, self.y + normalized[1])
            self.result_scalar[1] = 0
               

