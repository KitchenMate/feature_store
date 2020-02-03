from abc import abstractmethod
from config import config

import psycopg2
import pandas as pd
import numpy as np
import sqlalchemy as db

FEATURE_TABLE = 'list_of_features'

class Feature: 

    def connect(self, section):
        try:
            params = config(section)
            print('Connecting to database...')
            print(params['user'])
            engine = db.create_engine('postgresql://{0}:{1}@{2}:{3}/{4}'
                    .format(params['user'], params['password'], params['host'], params['port'], params['database']))

            print('postgresql://{0}:{1}@{2}:{3}/{4}'
                    .format(params['user'], params['password'], params['host'], params['port'], params['database']))
            conn = engine.connect()
            return engine, conn

        except Exception as e:
            print("Error connecting to database!, {}", e)
    
    def close(self, conn):
        if conn is not None:
            conn.close()
        print('Database connection closed.')

    def add_feature(self, name, tags, df):
        feature = pd.DataFrame(data={ 'name': name, 'tags': tags })
        feature.to_sql(name=FEATURE_TABLE, if_exists='append', con=self.fs_engine)
        df.to_sql(name=name, con=self.fs_engine)

    def get_feature(self, name):
        return pd.read_sql_table(name, con=self.fs_conn)

    def get_features(self, tag):
        pass

    def remove_feature(self, name):
        pass

    def __init__(self):
        self.fs_engine, self.fs_conn = self.connect("postgresql-fs")
        self.sup_engine, self.sup_conn = self.connect("postgresql-super")

    def __del__(self):
        self.close(self.fs_conn)
        self.close(self.sup_conn)

class RecipeToIngredient(Feature):

    def __init__(self):
        Feature.__init__(self)

    def create_feature(self):
        recipes = pd.read_sql_query(f"""
            select id, name from recipes
            where root_recipe_id = id
        """, con=self.sup_conn)
        self.add_feature("recipes_to_ingredients", ['recipe', 'test'], recipes)
        
    def read_feature(self):
        recipes = self.get_feature(FEATURE_TABLE)
        print(recipes)


a = RecipeToIngredient()
a.read_feature()
