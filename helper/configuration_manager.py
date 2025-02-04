import yaml
import os

def path_from_project_root(file_path: str) -> str:
    _root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return _root_dir + '/' + file_path

class ConfigurationManager:
    with open(path_from_project_root('resources/config.yaml'), 'rb') as __config_file:
        __configs = yaml.load(__config_file, Loader=yaml.FullLoader)

    @staticmethod
    def __config() -> dict:
        return ConfigurationManager.__configs

    @staticmethod
    def local_admin() -> dict:
        return ConfigurationManager.__configs['local.account']

    @staticmethod
    def write_tests_disabled() -> bool:
        return ConfigurationManager.__configs['write_tests_disabled'] == 'true'