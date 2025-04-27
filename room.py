import entity
import entities.player as player
import coords
import game_statistics

class Room:
    def __init__(self, size, coordinates, graphics):
        self.coordinates = coordinates
        self.require_teleport = False
        self.prevRoom = None
        self.teleport_coordinates = [0, 0]
        
        self.entities = []
        self.activatable_entities = []
        self.atackable_entities = []
        self.size = size
        self.graphics = graphics
        
        self.player = player.Player()
        self.player.initialize(self.graphics, self, (size[0] // 2) * self.graphics.cell_size, (size[0] // 2) * self.graphics.cell_size, None)
        self.entities.append(self.player)

     
    def activate_nearby(self):
        for entity in self.activatable_entities:
            if abs(entity.x - self.player.x) < 40 and abs(entity.y - self.player.y) < 40:
                entity.activate()
    
            
    def attack_nearby(self):
        for entity in self.atackable_entities:
            if abs(entity.x - self.player.x) < 40 and abs(entity.y - self.player.y) < 40:
                entity.give_damage(self.player.damage)


    def on_enabled(self):
        if self.prevRoom == None and game_statistics.location != [0, 0]:
            self.player.x = game_statistics.player_x
            self.player.y = game_statistics.player_y
            self.player.target_x = self.player.x
            self.player.target_y = self.player.y
        
        if self.prevRoom != None:
            coordsDiff = [self.prevRoom.coordinates[0] - self.coordinates[0], self.prevRoom.coordinates[1] - self.coordinates[1]]
            if coordsDiff[0] == -1:
                self.player.target_x = self.graphics.cell_size
            elif coordsDiff[0] == 1:
                self.player.target_x = (self.size[0] - 1) * self.graphics.cell_size - self.graphics.cell_size
            elif coordsDiff[0] == 0:
                self.player.target_x = self.prevRoom.player.target_x
            self.player.x = self.player.target_x

            if coordsDiff[1] == -1:
                self.player.target_y = self.graphics.cell_size
            elif coordsDiff[1] == 1:
                self.player.target_y = (self.size[1] - 1) * self.graphics.cell_size - self.graphics.cell_size
            elif coordsDiff[1] == 0:
                self.player.target_y = self.prevRoom.player.target_y
            self.player.y = self.player.target_y



    def on_update(self):
        if self.player.target_x <= 0:
            self.require_teleport = True
            self.teleport_coordinates = [self.coordinates[0] - 1, self.coordinates[1]]

        if self.player.target_x / self.graphics.cell_size >= self.size[0]:
            self.require_teleport = True
            self.teleport_coordinates = [self.coordinates[0] + 1, self.coordinates[1]]
        
        if self.player.target_y <= 0:
            self.require_teleport = True
            self.teleport_coordinates = [self.coordinates[0], self.coordinates[1] - 1]

        if self.player.target_y / self.graphics.cell_size >= self.size[0]:
            self.require_teleport = True
            self.teleport_coordinates = [self.coordinates[0], self.coordinates[1] + 1]

        for entity in self.entities:
            entity.on_update()       
