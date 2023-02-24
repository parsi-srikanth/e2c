import yaml


def read_config():
    config_file = open("config.yaml", 'r')
    config = yaml.safe_load(config_file)
    return config