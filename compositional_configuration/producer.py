from jsonargparse import ArgumentParser
from default_initializer import DefaultInitializer


class Producer(DefaultInitializer):
    @staticmethod
    def get_config_parser():

        parser = ArgumentParser()
        parser.add_argument("--start", type=int, default=0, help="Start of sequence")
        parser.add_argument("--end", type=int, default=10, help="End of sequence")
        return parser

    """ This makes the object callable: You can use it like this:
        producer = Producer(cfg)
        results = producer()
    """
    def __call__(self):
        return list(range(self.cfg.start, self.cfg.end))
