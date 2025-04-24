import entity
import entities.player as player
import coords

class Room:
    def __init__(self, size, coordinates, graphics):
        self.coordinates = coordinates
        self.requireTeleport = False
        self.prevRoom = None
        self.teleportCoordinates = [0, 0]
        
        self.entities = []
        self.activatableEntities = []
        self.size = size
        self.graphics = graphics
        
        self.player = player.Player()
        self.player.initialize(self.graphics, self, (size[0] // 2) * 35, (size[0] // 2) * 35, None)
        self.entities.append(self.player)
        
    def activate_nearby(self):
        for entity in self.activatableEntities:
            if (abs(entity.x - self.player.x) < 40 and abs(entity.y - self.player.y) < 40):
                entity.activate()

    def on_enabled(self):
        if self.prevRoom != None:
            coordsDiff = [self.prevRoom.coordinates[0] - self.coordinates[0], self.prevRoom.coordinates[1] - self.coordinates[1]]
            if coordsDiff[0] == -1:
                self.player.target_x = 35
            elif coordsDiff[0] == 1:
                self.player.target_x = (self.size[0] - 1) * 35
            elif coordsDiff[0] == 0:
                self.player.target_x = self.prevRoom.player.target_x
            self.player.x = self.player.target_x

            if coordsDiff[1] == -1:
                self.player.target_y = 35
            elif coordsDiff[1] == 1:
                self.player.target_y = (self.size[1] - 1) * 35            
            elif coordsDiff[1] == 0:
                self.player.target_y = self.prevRoom.player.target_y
            self.player.y = self.player.target_y

    def on_update(self):
        if self.player.target_x == 0:
            self.requireTeleport = True
            self.teleportCoordinates = [self.coordinates[0] - 1, self.coordinates[1]]

        if self.player.target_x / 35 == self.size[0]:
            self.requireTeleport = True
            self.teleportCoordinates =[self.coordinates[0] + 1, self.coordinates[1]]

        for entity in self.entities:
            entity.on_update()       
