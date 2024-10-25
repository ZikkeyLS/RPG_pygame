import coords

class Entity:
    def __init__(self):
        return

    def initialize(self, x, y, startup_image):
        self.x = x
        self.y = y
        self.image = startup_image
        self.coordinates = coords.to_number([x, y], self.graphics.grid_size[0])
        self.room.move_entity(self, x, y)
        return

    def post_move(self, x, y, coordinates):
        self.x = x
        self.y = y
        self.coordinates = coordinates

    def on_update(self):
        return
