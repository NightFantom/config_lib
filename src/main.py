

import yaml

from solution_config.config_factory import ConfigFactory

if __name__ == "__main__":
    conf_path = "/Users/denis/PycharmProjects/ConfigLib/example_config.yml"
    with open(conf_path, 'r') as f:
        config_dict = yaml.load(f)

    factory = ConfigFactory(config_dict)
    while True:
        config = factory.get_config("some_key")
        print(config["ttl"])