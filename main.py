import graphics
import world
import settings

graphics = graphics.Graphics()
graphics.initialize(settings.GRID_SIZE)

world = world.World()
world.initialize(settings.GRID_SIZE, graphics)

graphics.on_update_subscribers.append(world.on_update)
graphics.run()
