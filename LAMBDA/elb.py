import json

def lambda_handler(event, context):
    # TODO implement
    print(event)  #comprobar en cloudwatch
    return {

    "statusCode": 200,
    "statusDescription": "200 OK",
    "isBase64Encoded": False,
    "headers": {
        "Content-Type": "text/html"
    },
    "body": "<h1>Hello from Lambda!</h1>"

    }
