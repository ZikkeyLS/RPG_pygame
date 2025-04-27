from room import *
from entities.chest import *

class ChestRoom(Room):
    def __init__(self, size, coordinates, graphics):
        super().__init__(size, coordinates, graphics)
        
        self.chest = Chest()
        self.entities.append(self.chest)
        self.activatable_entities.append(self.chest)
        self.chest.initialize(graphics, self, (size[0] // 2) * graphics.cell_size, (size[0] // 2) * graphics.cell_size, None)

        pond_image = self.graphics.images["Pond"]
        
        pond1 = entity.Entity()
        pond1.initialize(graphics, self, 300, 150, pond_image)
        self.entities.append(pond1)
                  
        tree_image = self.graphics.images["Tree"]
        
        tree1 = entity.Entity()
        tree1.initialize(graphics, self, 200, 175, tree_image)
        self.entities.append(tree1)
                
        tree2 = entity.Entity()
        tree2.initialize(graphics, self, 425, 240, tree_image)
        self.entities.append(tree2)
        
        tree3 = entity.Entity()
        tree3.initialize(graphics, self, 250, 50, tree_image)
        self.entities.append(tree3)


    def on_update(self):
        super().on_update()
        self.graphics.render_text("Активируйте сундук", (300, 10))
        self.graphics.render_text("Назад", (self.graphics.cell_size * self.size[0] - self.graphics.cell_size * 2.25, 450), False)
