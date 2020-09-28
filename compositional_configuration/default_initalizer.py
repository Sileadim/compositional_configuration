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
