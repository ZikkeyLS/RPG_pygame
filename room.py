import entity
import player
import coords

class Room:
    def __init__(self, size, graphics):
        self.grid = []
        self.size = size
        self.graphics = graphics

        doors = []
        entities = {}

        for y in range(size[1]):
            self.grid.append([])
            for x in range(size[1]):
                self.grid[y].append([0])

        self.player = player.Player()
        self.player.graphics = graphics
        self.player.room = self
        self.player.initialize(size[0] // 2, size[1] // 2, self.graphics.images["WarriorIdle"])
        self.grid[size[0] // 2][size[1] // 2] = [1, self.player]

    def move_entity(self, entity_object, pos_x, pos_y):
        if pos_x < 0 or pos_y < 0 or pos_x >= self.size[0] or pos_y >= self.size[1]:
            return False
        coordinates = coords.to_number([pos_x, pos_y], self.size[0])
        self.grid[entity_object.x][entity_object.y] = [0]
        self.grid[pos_x][pos_y] = [1, entity_object]

        # set new image

        #self.graphics.canvas.itemconfig(self.graphics.get_cell(coordinates)[1], image=entity_object.image)
        #if coordinates != entity_object.coordinates:
        #    self.graphics.canvas.itemconfig(self.graphics.get_cell(entity_object.coordinates)[1], image=self.graphics.images["Empty"])
        #self.graphics.get_cell(coordinates)[1].configure(image=entity_object.image)
        entity_object.post_move(pos_x, pos_y, coordinates)
        return True

    def on_update(self):
        perform_on = []
        for y in range(self.size[1]):
            for x in range(self.size[1]):
                if self.grid[y][x][0] == 1:
                    perform_on.append(self.grid[y][x][1])        
        for i in range(len(perform_on)):
            perform_on[i].on_update()
