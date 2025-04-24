from room import *
from entities.chest import *

class ChestRoom(Room):
    def __init__(self, size, coordinates, graphics):
        super().__init__(size, coordinates, graphics)
        
        self.chest = Chest()
        self.chest.initialize(graphics, self, (size[0] // 2) * graphics.cell_size, (size[0] // 2) * graphics.cell_size, None)
        self.entities.append(self.chest)
        self.activatableEntities.append(self.chest)
