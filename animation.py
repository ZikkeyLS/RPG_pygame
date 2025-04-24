
class Animation:
    def __init__(self, animation_images, speed = 1):
        self.current_frame = 0
        self.last_frame = 0
        self.animation_frames = animation_images
        self.speed = speed

    def Restart(self):
        self.current_frame = 0

    def RunFrame(self, entity):
        entity.image = self.animation_frames[round(self.current_frame)]
        self.last_frame = round(self.current_frame)
        
        self.current_frame += self.speed

        if round(self.current_frame) >= len(self.animation_frames):
            self.current_frame = 0
            return True
        if round(self.current_frame) < 0:
            self.current_frame = len(self.animation_frames - 1)
            return True

        return False
