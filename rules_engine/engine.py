import yaml


class Engine():
    def __init__(self, config_file):
        config = yaml.load(open(config_file))
        print(config)
