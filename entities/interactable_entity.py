from entity import *

class InteractableEntity(Entity):   
    def activate(self):
        self.on_activate()
        
    def on_activate(self):
        return
