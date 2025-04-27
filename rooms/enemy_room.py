from room import *
from entities.player import *
from entities.enemy import *

class EnemyRoom(Room):
    def __init__(self, size, coordinates, graphics):
        super().__init__(size, coordinates, graphics)
          
        tree_image = self.graphics.images["Tree"]
        
        tree1 = entity.Entity()
        tree1.initialize(graphics, self, 250, 250, tree_image)
        self.entities.append(tree1)
        
        enemy = Enemy()        
        self.entities.append(enemy)
        self.atackable_entities.append(enemy)
        enemy.initialize(graphics, self, (size[0] // 2) * self.graphics.cell_size, (size[0] // 2) * self.graphics.cell_size, None)


    def on_update(self):
        super().on_update()
        self.graphics.render_text("Назад", (425, 10), False)
