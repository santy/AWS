import json
import os

def lambda_handler(event, context):
    # TODO implement
    time.sleep(2)
    return os.getenv("ENTORNO_VARIABLE")
