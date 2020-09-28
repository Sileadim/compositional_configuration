from manager import Manager

if __name__ == "__main__":

    # just initializing without anything gives you the default
    default_manager = Manager()
    results = default_manager()
    print(results)

    # we get the cfg as a namespace object and set the values directly
    cfg = Manager.get_config_parser().get_defaults()
    cfg.producer.start = 10
    cfg.producer.end = 20
    manager = Manager(cfg)
    results = manager()
    print(results)