try:
    from application.sample import Sample
except ModuleNotFoundError as init:
    from sampler.application.sample import Sample
finally:
    from collections import deque
    import logging, math, time


logging.basicConfig(level=logging.INFO, format='%(message)s')


class Repeater:

    LOOPING  = False
    STATE    = 0
    SENTINAL = 0

    def __init__(self, resource):
        self.resource = resource
        self.rate = 0.05
        self.deque = deque(maxlen=3)
        self.deque.append(Sample(resource))
        self.deque.append(Sample(resource))
        self.fade = self.deque[0].fade_point
        self.chain = 0

    def play(self):
        self.deque[0].sound.set_volume(1)
        self.deque[0].sound.play()
        while float('inf'):
            self.delegation()
    
    def stop(self):
        for sample in self.deque:
            sample.stop()

    def delegation(self):
        recycle = self.fade <= self.chain <= self.fade + .32
        logging.debug(
                f'[REPEAT]: {recycle}'
                f'    {self.fade} <= {self.chain} <='
                f' ({self.fade} + .32)'
                )

        if recycle: self.recycler()

        if Repeater.LOOPING: self.cross_fade()

        self.chain = (self.chain + 0.33) % (self.fade + 1)
        time.sleep(0.33)
   
    def recycler(self):
        Repeater.LOOPING = True
        Repeater.STATE = 0 if Repeater.STATE else 1
        self.deque.append(Sample(self.resource))
        self.deque[1].sound.play()
        logging.debug(f'STATE: {Repeater.STATE}')

    def cross_fade(self):
        if self.deque[1].sound.get_volume != 1:
            self.deque[1].sound.set_volume(
                    self.deque[1].sound.get_volume() + self.rate
                    )
        if self.deque[0].sound.get_volume != 0:
            self.deque[0].sound.set_volume(
                    self.deque[0].sound.get_volume() - self.rate
                    )


if __name__ == '__main__':
    resource = '../resources/test.wav'
    repeater = Repeater(resource)
    try:
        repeater.play()
    except KeyboardInterrupt as stop:
        repeater.stop()
        logging.info(f'Halted repeater.loop() process for {resource}')
