import logging
import configparser
import os

def load_config(config_path="config.ini"):
    config = configparser.ConfigParser()
    if os.path.exists(config_path):
        config.read(config_path)
        logging.info(f"Configuration loaded from file: {config_path}")
    else:
        logging.warning(f"Configuration file not found: {config_path}. Using default values.")
    return config

def get_config_section(config, section_name):
    if config.has_section(section_name):
        return dict(config.items(section_name))
    else:
        logging.warning(f"Section '{section_name}' not found in configuration.")
        return {}
