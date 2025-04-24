import coords
from rooms.default_room import *
from rooms.chest_room import *
import game_statistics

class World:
    def initialize(self, settings, graphics):
        global grid_size
        grid_size = settings

        self.rooms = {}
        self.graphics = graphics

        initialRoom = DefaultRoom(grid_size, [5, 5], graphics)
        self.rooms[coords.to_number([5, 5], 10)] = initialRoom

        secondRoom = ChestRoom(grid_size, [4, 5], graphics)
        self.rooms[coords.to_number([4, 5], 10)] = secondRoom

        self.currentRoom = None
        self.prevRoom = None
        self.setCurrentRoom(initialRoom)
    
    def setCurrentRoom(self, room):
        self.prevRoom = self.currentRoom
        self.currentRoom = room
        self.currentRoom.prevRoom = self.prevRoom
        self.currentRoom.on_enabled()

    def on_update(self):
        self.graphics.render_text("Деньги (" + str(game_statistics.money) + ")", (30, 10))
        
        if (self.currentRoom.requireTeleport):
            self.currentRoom.requireTeleport = False
            if coords.to_number(self.currentRoom.teleportCoordinates, 10) in self.rooms:
                self.setCurrentRoom(self.rooms[coords.to_number(self.currentRoom.teleportCoordinates, 10)])

        self.currentRoom.on_update()
