from flask import Flask
from celery import Celery
from config import config

params = config('redis')
redis_url = 'redis://{0}:{1}@{2}:{3}'.format(params['username'], params['password'], params['hostname']. params['port']

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = redis_url
app.config['CELERY_RESULT_BACKEND'] = redis_url

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


