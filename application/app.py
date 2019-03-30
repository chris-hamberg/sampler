try:
    from application.sample import Sample
    from application.repeater import Repeater
except ModuleNotFoundError as init:
    from sampler.application.sample import Sample
    from sampler.application.repeater import Repeater
finally:
    from pprint import pprint
    import pathlib, sys, os


class Resource:

    PATH = os.path.join('sampler', 'resources')

    def __init__(self):
        self.play_list = {e:
                os.path.join(Resource.PATH, sample
                ) for e, sample in enumerate(os.listdir (
                Resource.PATH
                    ))}

    def play(self, sample):
        sample = self.process(sample)
        try:
            sample.play()
            while True: pass
        except KeyboardInterrupt as stop:
            sample.stop()

    def process(self, sample):
        if pathlib.Path(sample).stem.endswith('R'):
            sample = Repeater(sample)
        else:
            sample = Sample(sample)
        return sample

    def automated(self):
        sample, name = -1, None
        while float('inf'):
            try:
                os.system('clear')
                pprint(self)
                selection = input(f'[QUE]: {name}\n>>> ')
                if selection:
                    sample = int(selection)
                target = self.play_list.get(sample, 0)
                name = pathlib.Path(target.split(os.sep)[-1]).stem
                print(f'Now playing {name}')
                self.play(target)
                name = pathlib.Path(
                        self.play_list[sample+1].split(os.sep)[-1]
                        ).stem if sample+1 <= len(self.play_list.keys()
                        ) else None
            except (KeyError, ValueError, AttributeError) as invalid:
                if selection == 'q':
                    sys.exit('Good bye')
                name = None
            else:
                sample += 1

    def __repr__(self):
        return str({
            k: pathlib.Path(name.split(os.sep)[-1]).stem 
            for k, name in self.play_list.items(
                )})


def main():
    resource = Resource()
    while float('inf'):
        resource.automated()


if __name__ == '__main__':
    main()
