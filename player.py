import entity
from input_bindings import *
import input_bindings

class Player(entity.Entity):
    def on_update(self):
        result_scalar = [0, 0]

        if is_pressed(K_LEFT):
            result_scalar[0] -= 1
        elif is_pressed(K_RIGHT):
            result_scalar[0] += 1
        if is_pressed(K_UP):
            result_scalar[1] -= 1
        elif is_pressed(K_DOWN):
            result_scalar[1] += 1

        self.room.move_entity(self, self.x + result_scalar[0], self.y + result_scalar[1])
