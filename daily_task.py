import json

def lambda_handler(event, context):

   perform_daily()

    return {
        'statusCode': 200,
        'body': json.dumps("Daily Function Executed Well")
    }

def perform_daily()
    print("Starting daily task")
    print("Finished daily task")