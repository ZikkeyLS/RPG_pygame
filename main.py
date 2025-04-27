import graphics
import world
import settings

graphics = graphics.Graphics()
graphics.initialize(settings.GRID_SIZE)
gameWorld = world.World()
graphics.world = gameWorld
graphics.run()
