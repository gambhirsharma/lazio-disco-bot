import json
import requests
from datetime import datetime

# Initialize the global run_count variable
run_count = 0


def lambda_handler(event, context):

# print("Hello World")
# print(f"date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

global run_count
run_count += 1

return {
    "statusCode": 200,
    "body": json.dumps({
        "message": "the function is running",
        "time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "run_count": run_count,
        # "location": ip.text.replace("\n", "")
    }),
}
