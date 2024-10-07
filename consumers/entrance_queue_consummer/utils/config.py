import toml


class Configs:

    def __init__(self):
        pass

    @staticmethod
    def get_api_configs(config_path: str) -> dict:

        config = toml.load(config_path)

        api_config: dict = config['API_CLASSIFIER']

        return api_config
