import json

def lambda_handler(event, context):
  print(event)
  record = event['Records']

  for record in records:
    body = record['Body']
    print(body)
