from jsonargparse import ArgumentParser
from default_initalizer import DefaultInitializer


class Transformer(DefaultInitializer):
    @staticmethod
    def get_config_parser():

        parser = ArgumentParser()
        parser.add_argument("--factor", type=int, default=2, help="Factor to multiply")
        return parser

    def __call__(self, list_to_be_transformed):
        return [i * self.cfg.factor for i in list_to_be_transformed]
