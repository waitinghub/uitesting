from configparser import ConfigParser
from common.handle_path import CONF_FILE

def config_handler():
    config = ConfigParser()
    config.read(CONF_FILE, encoding='utf8')
    return config

read_config = config_handler()