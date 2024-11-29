import coords

class Entity:
    def __init__(self):
        return

    def initialize(self, inner_graphics, current_room, x, y, startup_image):
        self.graphics = inner_graphics
        self.room = current_room
        self.x = x
        self.y = y
        self.image = startup_image
        self.coordinates = coords.to_number([x, y], self.graphics.grid_size[0])

        self.post_initialize()

    def post_initialize(self):
        return

    def on_update(self):
        return
