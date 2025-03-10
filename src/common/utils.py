import logging
import datetime
import json
import os

def setup_logging(log_level=logging.INFO):
    logging.basicConfig(level=log_level,
                        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

def get_timestamp_str():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_json_config(config_path):
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {config_path}")
        return None
    except json.JSONDecodeError:
        logging.error(f"Error parsing JSON config file: {config_path}")
        return None

def create_directory_if_not_exists(dir_path):
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
            logging.info(f"Created directory: {dir_path}")
        except OSError as e:
            logging.error(f"Error creating directory: {e}")
    elif not os.path.isdir(dir_path):
        logging.error(f"Path '{dir_path}' exists but is not a directory.")
