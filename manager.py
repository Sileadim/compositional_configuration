from jsonargparse import ArgumentParser, ActionParser
from abc import abstractmethod


class DefaultInitializer:
    @staticmethod  # This makes this method a class method: It can be called on the class object itself
    @abstractmethod  # This forces all the child classes to implement this method
    def get_config_parser():
        pass

    # we make cfg=None, so it becomes optional
    def __init__(self, cfg=None):
        # if no cfg was passed, we use the default one
        if not cfg:
            """We call this method on the instance's class, which is going to be the child's class.
            This removes boilerplate code, as we only have to write it once here.
            Alternatively we could omit this whole super class and inside e.g. Producer we call
            self.Producer.get_config_parser().get_defaults()
            """
            cfg = (
                self.__class__.get_config_parser().get_defaults()  # get defaults return the parsed config
            )
            self.cfg = cfg
        else:
            self.cfg = cfg


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


class Transformer(DefaultInitializer):
    @staticmethod
    def get_config_parser():

        parser = ArgumentParser()
        parser.add_argument("--factor", type=int, default=2, help="Factor to multiply")
        return parser

    def __call__(self, list_to_be_transformed):
        return [i * self.cfg.factor for i in list_to_be_transformed]


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