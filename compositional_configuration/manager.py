from jsonargparse import ArgumentParser, ActionParser
from default_initalizer import DefaultInitializer
from producer import Producer
from transformer import Transformer

class Manager(DefaultInitializer):
    @staticmethod
    def get_config_parser():

        parser = ArgumentParser()
        parser.add_argument(
            "--producer", action=ActionParser(parser=Producer.get_config_parser())
        )
        parser.add_argument(
            "--transformer", action=ActionParser(parser=Transformer.get_config_parser())
        )
        return parser

    def __init__(self, cfg=None):
        # we call the init of DefaultIntializer directly to initialize self.cfg
        super().__init__(cfg=cfg)
        # we init our variables with the corresponding parts of the config
        self.producer = Producer(self.cfg.producer)
        self.transformer = Transformer(self.cfg.transformer)

    def __call__(self):

        list_to_be_transformed = self.producer()
        return self.transformer(list_to_be_transformed)


if __name__ == "__main__":

    parser = Manager.get_config_parser()
    cfg = parser.parse_args()
    manager = Manager(cfg)
    results = manager()
    print(results)