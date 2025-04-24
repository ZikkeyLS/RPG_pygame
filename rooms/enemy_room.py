from room import *
from entities.player import *

class EnemyRoom(Room):
    def __init__(self, size, coordinates, graphics):
        super().__init__(size, coordinates, graphics)
          
        tree_image = self.graphics.images["Tree"]
        
        tree1 = entity.Entity()
        tree1.initialize(graphics, self, 250, 250, tree_image)
        self.entities.append(tree1)


    def on_update(self):
        super().on_update()
        self.graphics.render_text("Назад", (425, 10), False)
