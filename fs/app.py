from fs.config import config as cfg
from fs.database import Database

from celery import Celery
from celery.schedules import cronttab

import boto3
import pandas as pd

app = Celery('Feature Store (Job Scheduling)',
             broker=cfg['REDIS_URL'],
             backend=cfg['REDIS_URL'])

# Databases
feature_store = Database(cfg['DATABASE_URL'])

if __name__ == '__main__':
    app.start()

def load_module(module):
    module_path = module

    if module_path in sys.modules:
        return sys.modules[module_path]

    return __import__(module_path, fromList=[module])


#def connect_to_s3():
#    s3 = boto3.resource('s3')
#    bucket = s3.Bucket('kitchenmate-jupyter')
#    for obj in bucket.objects.all():
#        print(obj)
#connect_to_s3()


