import entity
from input_bindings import *
import animation
import game_statistics

class Player(entity.Entity):
    def post_initialize(self):
        self.move_frames = 20
        self.result_scalar = [0, 0]
        self.target_x = self.x
        self.target_y = self.y

        self.damage = 2

        idle_animation_frames = self.compile_idle_animation()
        self.idle_animation = animation.Animation(idle_animation_frames, 1 / len(idle_animation_frames))

        walk_animation_frames = self.compile_walk_animation()
        self.walk_animation = animation.Animation(walk_animation_frames, 1 / len(walk_animation_frames))
        
        attack_animation_frames = self.compile_attack_animation()
        self.attack_animation = animation.Animation(attack_animation_frames, 1 / len(attack_animation_frames))        
        
        self.current_animation = self.idle_animation
        self.attacking = False


    def compile_attack_animation(self):
        result_animation = []
        idle_animation_atlas = self.graphics.get_raw_image("assets/images/Warrior_1/Attack_1.png")
        for i in range(4):
            result_animation.append(self.graphics.compile_atlas_image(idle_animation_atlas, 70, 35, 96, 53, 13 + (i * 96), 44))
        return result_animation


    def compile_idle_animation(self):
        result_animation = []
        idle_animation_atlas = self.graphics.get_raw_image("assets/images/Warrior_1/Idle.png")
        for i in range(6):
            result_animation.append(self.graphics.compile_atlas_image(idle_animation_atlas, 30, 35, 37, 48, 29 + (i * 96), 48))
        return result_animation


    def compile_walk_animation(self):
        result_animation = []
        walk_animation_atlas = self.graphics.get_raw_image("assets/images/Warrior_1/Walk.png")
        for i in range(8):
            result_animation.append(self.graphics.compile_atlas_image(walk_animation_atlas, 30, 35, 37, 48, 29 + (i * 96), 48))
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
        horizontal = 0
        vertical = 0
        
        game_statistics.player_x = self.x
        game_statistics.player_y = self.y
        
        if is_down(K_e):
            self.room.activate_nearby()
            
        if is_down(K_SPACE):
            self.room.attack_nearby()
            self.attacking = True

        if is_pressed(K_a):
            horizontal -= 1
        elif is_pressed(K_d):
            horizontal += 1
        if is_pressed(K_w):
            vertical -= 1
        elif is_pressed(K_s):
            vertical += 1

        scale = 1
        if horizontal != 0 and vertical != 0:
            scale = 0.5

        self.result_scalar[0] += horizontal * scale
        self.result_scalar[1] += vertical * scale

        self.moving = is_pressed(K_a) or is_pressed(K_d) or is_pressed(K_w) or is_pressed(K_s)

        if is_pressed(K_a):
            self.size_x = -1
        else:
            self.size_x = 1
            
        last_frame = self.current_animation.RunFrame(self)
                    
        if self.attacking:
            if self.current_animation != self.attack_animation:
                self.current_animation = self.attack_animation
            else:
                if last_frame:
                    self.current_animation = self.idle_animation
                    self.attacking = False

        if not(self.attacking):
            if not self.moving:
                self.current_animation = self.idle_animation
            else:
                self.current_animation = self.walk_animation

        self.x = self.lerp(self.x, self.target_x, 1 / 10)
        self.y = self.lerp(self.y, self.target_y, 1 / 10)

        if abs(self.result_scalar[0]) >= self.move_frames and abs(self.result_scalar[1]) > self.move_frames:
            self.target_x += self.result_scalar[0] / self.move_frames * 35
            self.target_y += self.result_scalar[1] / self.move_frames * 35
            self.result_scalar = [0, 0]
        elif abs(self.result_scalar[0]) >= self.move_frames:
            self.target_x += self.result_scalar[0] / self.move_frames * 35
            self.result_scalar[0] = 0
        elif abs(self.result_scalar[1]) >= self.move_frames:
            self.target_y += self.result_scalar[1] / self.move_frames * 35
            self.result_scalar[1] = 0

        if self.target_x < 0:
            self.target_x = 0
        elif self.x > self.room.size[0] * self.graphics.cell_size:
            self.target_x = self.room.size[0] * self.graphics.cell_size
        if self.target_x < 0:
            self.target_x = 0
        elif self.target_x > self.room.size[1] * self.graphics.cell_size:
            self.target_x = self.room.size[1] * self.graphics.cell_size

        if self.x < 0:
            self.x = 0
        elif self.x > self.room.size[0] * self.graphics.cell_size - self.graphics.cell_size:
            self.x = self.room.size[0] * self.graphics.cell_size - self.graphics.cell_size
        if self.y < 0:
            self.y = 0
        elif self.y > self.room.size[1] * self.graphics.cell_size - self.graphics.cell_size:
            self.y = self.room.size[1] * self.graphics.cell_size - self.graphics.cell_size
