import json
import os

def lambda_handler(event, context):
    # TODO implement
    return os.getenv("ENTORNO_VARIABLE")
