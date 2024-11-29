import entity
from input_bindings import *
import input_bindings
import animation

class Player(entity.Entity):

    def post_initialize(self):
        self.moveFrames = 20
        self.result_scalar = [0, 0]
        self.target_x = self.x
        self.target_y = self.y

        idle_animation_frames = self.compile_idle_animation()
        self.idleAnimation = animation.Animation(idle_animation_frames, 1 / len(idle_animation_frames))

    def compile_idle_animation(self):
        result_animation = []
        idle_animation_atlas = self.graphics.get_raw_image("assets/images/Warrior_1/Idle.png")
        for i in range(6):
            result_animation.append(self.graphics.compile_atlas_image(idle_animation_atlas, 30, 35, 37, 48, 29 + (i * 96), 48))
        return result_animation

    def lerp(self, a: float, b: float, t: float) -> float:
        return (1 - t) * a + t * b

    def move_towards(self, a: float, b: float, t: float) -> float:
        if a == b:
            return a

        direction = 0
        if a - b < 0:
            direction = 1
        else:
            direction = -1
    
        return round(a + direction, 2)

    def on_update(self):
        if is_pressed(K_LEFT):
            self.result_scalar[0] -= 1
        elif is_pressed(K_RIGHT):
            self.result_scalar[0] += 1
        if is_pressed(K_UP):
            self.result_scalar[1] -= 1
        elif is_pressed(K_DOWN):
            self.result_scalar[1] += 1

        self.x = self.lerp(self.x, self.target_x, 1 / 10)
        self.y = self.lerp(self.y, self.target_y, 1 / 10)

        if abs(self.result_scalar[0]) >= self.moveFrames and abs(self.result_scalar[1]) > self.moveFrames:
            self.target_x += self.result_scalar[0] / self.moveFrames * 30
            self.target_y += self.result_scalar[1] / self.moveFrames * 35
            self.result_scalar = [0, 0]
        elif abs(self.result_scalar[0]) >= self.moveFrames:
            self.target_x += self.result_scalar[0] / self.moveFrames * 30
            self.result_scalar[0] = 0
        elif abs(self.result_scalar[1]) >= self.moveFrames:
            self.target_y += self.result_scalar[1] / self.moveFrames * 35
            self.result_scalar[1] = 0

        if self.target_x < 0:
            self.target_x = 0
        elif self.x > self.room.size[0] * 30:
            self.target_x = self.room.size[0] * 30
        if self.target_x < 0:
            self.target_x = 0
        elif self.target_x > self.room.size[1] * 35:
            self.target_x = self.room.size[1] * 35

        if self.x < 0:
            self.x = 0
        elif self.x > self.room.size[0] * 30:
            self.x = self.room.size[0] * 30
        if self.y < 0:
            self.y = 0
        elif self.y > self.room.size[1] * 35:
            self.y = self.room.size[1] * 35

        self.idleAnimation.RunFrame(self)
