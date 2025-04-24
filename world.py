import coords
from rooms.default_room import *
from rooms.chest_room import *
from rooms.replication_room import *
from rooms.enemy_room import *
import game_statistics

class World:
    def initialize(self, settings, graphics):
        global grid_size
        grid_size = settings

        self.rooms = {}
        self.graphics = graphics

        initial_room = DefaultRoom(grid_size, [5, 5], graphics)
        self.rooms[coords.to_number([5, 5], 10)] = initial_room

        secondRoom = ChestRoom(grid_size, [4, 5], graphics)
        self.rooms[coords.to_number([4, 5], 10)] = secondRoom
        
        thirdRoom = ReplicationRoom(grid_size, [6, 5], graphics)
        self.rooms[coords.to_number([6, 5], 10)] = thirdRoom
        
        fourthRoom = EnemyRoom(grid_size, [5, 6], graphics)
        self.rooms[coords.to_number([5, 6], 10)] = fourthRoom

        self.current_room = None
        self.prev_room = None
        self.setCurrentRoom(initial_room)

  
    def setCurrentRoom(self, room):
        self.prev_room = self.current_room
        self.current_room = room
        self.current_room.prevRoom = self.prev_room
        self.current_room.on_enabled()


    def on_update(self):
        self.graphics.render_text("Деньги (" + str(game_statistics.money) + ")", (30, 10))
        
        if (self.current_room.require_teleport):
            self.current_room.require_teleport = False
            if coords.to_number(self.current_room.teleport_coordinates, 10) in self.rooms:
                self.setCurrentRoom(self.rooms[coords.to_number(self.current_room.teleport_coordinates, 10)])

        self.current_room.on_update()
