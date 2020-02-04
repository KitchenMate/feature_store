from fs.database import Database
from fs.config import config as cfg

class Feature: 
    def __init__(self):
        self.feature_store = Database(cfg['DATABASE_URL'])
        self.fridge = Database(cfg['SCIENCE_URL'])

    def create_feature():
        raise NotImplementedError("Please implement a create_feature() method, that returns a singular dataframe")


