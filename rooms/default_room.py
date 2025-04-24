from room import *

class DefaultRoom(Room):
    def __init__(self, size, coordinates, graphics):
        super().__init__(size, coordinates, graphics)
          
        tree_image = self.graphics.images["Tree"]
        
        tree1 = entity.Entity()
        tree1.initialize(graphics, self, 250, 250, tree_image)
        self.entities.append(tree1)
        
        tree2 = entity.Entity()
        tree2.initialize(graphics, self, 583, 475, tree_image)
        self.entities.append(tree2)
        
        tree3 = entity.Entity()
        tree3.initialize(graphics, self, 100, 600, tree_image)
        self.entities.append(tree3)

        tree4 = entity.Entity()
        tree4.initialize(graphics, self, 600, 175, tree_image)
        self.entities.append(tree4)
        
        tree5 = entity.Entity()
        tree5.initialize(graphics, self, 450, 700, tree_image)
        self.entities.append(tree5)

    def on_update(self):
        super().on_update()
        self.graphics.render_text("Двигайтесь до упора влево", (250, 10))
