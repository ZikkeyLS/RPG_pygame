
class Animation:
    def __init__(self, animationImages, room):
        self.currentFrame = 0
        self.animationFrames = animationImages
        self.speed = 1

    def Restart(self):
        self.currentFrame = 0
    
    def RunFrame(self, entity):
        self.currentFrame += self.speed
        if self.currentFrame >= len(self.animationFrames):
            self.currentFrame = 0
        if self.currentFrame < 0:
            self.currentFrame = len(self.animationFrames - 1)
        self.room.update_image(entity)