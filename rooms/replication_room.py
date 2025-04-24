from room import *
from entities.player import *

class ReplicationRoom(Room):
    def __init__(self, size, coordinates, graphics):
        super().__init__(size, coordinates, graphics)
          
        tree_image = self.graphics.images["Tree"]
        
        tree1 = entity.Entity()
        tree1.initialize(graphics, self, 250, 250, tree_image)
        self.entities.append(tree1)
        
        for i in range(3):
            player = Player()
            player.initialize(self.graphics, self, (size[0] // 2) * self.graphics.cell_size + self.graphics.cell_size * i, 
                              (size[0] // 2) * self.graphics.cell_size + self.graphics.cell_size * i, None)
            self.entities.append(player)
            
        for i in range(3):
            player = Player()
            player.initialize(self.graphics, self, (size[0] // 2) * self.graphics.cell_size - self.graphics.cell_size * i, 
                              (size[0] // 2) * self.graphics.cell_size + self.graphics.cell_size * i, None)
            self.entities.append(player)


    def on_update(self):
        super().on_update()
        self.graphics.render_text("Двигайтесь до упора влево", (250, 10))
