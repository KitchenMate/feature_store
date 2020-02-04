import sqlalchemy as db
import pandas as pd
import numpy as np

from fs.config import config as cfg

class Database: 
    def __init__(self, uri):
        self.engine, self.conn = self.connect(uri)
    
    def __del__(self):
        self.close(self.conn)
    
    def connect(self, uri):
        print(uri)
        try:
            print('Connecting to database...')
            engine = db.create_engine(uri)
            conn = engine.connect()
            return engine, conn
    
        except Exception as e:
            print("Error connecting to database!, {}", e)

        return None, None
    
    def close(self, conn):
        if conn is not None:
            conn.close()
        print('Database connection closed.')
