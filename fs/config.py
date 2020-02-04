import configparser
import os

# TODO: Swap names of database and feature_store (very confusing)

config = configparser.ConfigParser()
config.optionxform = str # Keep keys in uppercase
config.read('config/config.ini')

config = dict(config.items('DEFAULT'))


def replace_if_exists(env_var):
    if env_var in os.environ:
        config[env_var] = os.environ[env_var]

replace_if_exists('DATABASE_URL')
replace_if_exists('REDIS_URL')
replace_if_exists('SCIENCE_URL')


