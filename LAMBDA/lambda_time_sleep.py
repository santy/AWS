import json
import os
import time


def connect_to_db():
    time.sleep(2)
    
    
connect_to_db()


def lambda_handler(event, context):
    # TODO implement
    #connect_to_db()
    return os.getenv("ENTORNO_VARIABLE")
