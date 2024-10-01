import toml


class Configs:

    def __init__(self):
        pass

    @staticmethod
    def get_database_configs(config_path: str) -> dict:

        config = toml.load(config_path)

        db_config: dict = config['database']

        return db_config

    @staticmethod
    def get_model_version(config_path: str):
        config = toml.load(config_path)

        model_config: dict = config['model']

        return model_config

    @staticmethod
    def get_image_camera(config_path: str):
        config = toml.load(config_path)

        img_config: dict = config['image']

        return img_config
