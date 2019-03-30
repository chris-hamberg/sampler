import pathlib, pygame, os


pygame.mixer.init()
pygame.init()


class Sample:

    def __init__(self, resource='../resources/test.wav'):
        self.name = pathlib.Path(resource.split(os.sep)[-1]).stem
        self.sound = pygame.mixer.Sound(resource)
        self.sound.set_volume(0)
        self.terminus = self.sound.get_length()
        self.fade_point = int(self.terminus - self.terminus / 3)
                
    def play(self):
        self.sound.set_volume(1)
        self.sound.play()

    def stop(self):
        self.sound.stop()

    def __repr__(self):
        return self.name
        
if __name__ == '__main__':
    sample = Sample()
    sample.play()
