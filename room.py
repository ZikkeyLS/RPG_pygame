import entity
import player
import coords

class Room:
    def __init__(self, size, graphics):
        self.entities = []
        self.size = size
        self.graphics = graphics

        doors = []

        self.player = player.Player()
        self.player.initialize(self.graphics, self, (size[0] // 2) * 30, (size[0] // 2) * 35, self.graphics.images["WarriorIdle"])

        self.entities.append(self.player)

    def on_update(self):
        for entity in self.entities:
            entity.on_update()       
