import json

def lambda_handler(event, context):
    print(event)       #comprobar en cloudwatch que el metodo obtenido es a traves de GET
    body = "Hello From Lambda!"
    statusCode = 200
    return {
        "statusCode": statusCode,
        "body": json.dumps(body),
        "headers": {
            "Content-Type":"application/json"
        }
    }
