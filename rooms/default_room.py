from room import *

class DefaultRoom(Room):
    def __init__(self, size, coordinates, graphics):
        super().__init__(size, coordinates, graphics)

    def on_update(self):
        super().on_update()
        self.graphics.render_text("Двигайтесь до упора влево", (250, 10))
