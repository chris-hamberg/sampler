from application.app import Resource
import sys, os


PLAY_LIST_DIR = 'resources'


def main():
    try:
        resource = Resource()
        resource.PATH = os.path.join('sampler', PLAY_LIST_DIR)
        while float('inf'):
            resource.automated()
    except KeyboardInterrupt as finished:
        sys.exit('Good bye.')


if __name__ == '__main__':
    main()
