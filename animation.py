
class Animation:
    def __init__(self, animationImages, speed = 1):
        self.currentFrame = 0
        self.lastFrame = 0
        self.animationFrames = animationImages
        self.speed = speed

    def Restart(self):
        self.currentFrame = 0
    
    def RunFrame(self, entity):
        self.currentFrame += self.speed

        if round(self.currentFrame) >= len(self.animationFrames):
            self.currentFrame = 0
        if round(self.currentFrame) < 0:
            self.currentFrame = len(self.animationFrames - 1)

        if abs(self.currentFrame - self.lastFrame) < 1:
            return

        entity.image = self.animationFrames[round(self.currentFrame)]
        self.lastFrame = round(self.currentFrame)
