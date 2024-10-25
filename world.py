import room

class World:
    def initialize(self, settings, graphics):
        global grid_size
        grid_size = settings

        self.currentRoom = room.Room(grid_size, graphics)

    def on_update(self):
        self.currentRoom.on_update()
