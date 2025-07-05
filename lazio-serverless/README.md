# lazio-serverless

### My learning: 
- You need to `sam build` for every change you make in the code.
- check if `tempate.yaml` is correct by using `sam validate --lint`
- `sam local` to test everything locally
- `sam local invoke` to test a single function locally
- `sam local start-lambda` to deploy the code to AWS

- Use this command to invoke the function when it's running locally using `sam local start-lambda`: 
```bash
aws lambda invoke --endpoint-url http://127.0.0.1:3001 --function-name HelloWorldFunction out.json

```

---
#### Triggers for Lambda functions:
[EventSource](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-eventsource.html)

AlexaSkill, Api, CloudWatchEvent, CloudWatchLogs, Cognito, DocumentDB, DynamoDB, EventBridgeRule, HttpApi, IoTRule, Kinesis, MQ, MSK, S3, Schedule, ScheduleV2, SelfManagedKafka, SNS, SQS



---

AWS SAM does not support the `.env` convention. Read this [blog](https://blowstack.com/blog/how-to-use-environmental-variables-in-aws-sam) for more info

---

Copy `.env.example` to `.env` and fill in your AWS credentials.
Run `source .env` in your terminal before using the AWS CLI with this project.
