# Serverless Application

AWS CloudFormation, featuring DynamoDB, Lambda functions, and API Gateway for feedback collection and usage tracking.

## Architecture

This application consists of:

- **1 Lambda Functions** (Python 3.12)
  - `feedback_collection` - Handles feedback data collection
  - `get_alias_promt` - Retrieves alias prompts
  - `updateusage` - Updates usage statistics

- **2 DynamoDB Tables**
  - `feedback-collection` - Stores feedback data
  - `usage-collection` - Stores usage tracking data

- **3 API Gateway Endpoints**
  - HTTP API for feedback collection
  - REST API for alias prompts
  - REST API for usage updates

## Prerequisites

- AWS CLI configured with appropriate permissions

## Deployment

### Step 1: Package the Application

Package your CloudFormation template and upload code to S3:

```bash
aws cloudformation package \
  --template-file template.yaml \
  --s3-bucket YOUR_BUCKET_NAME \
  --output-template-file packaged-template.yaml
```

**Note:** Replace `YOUR_BUCKET_NAME` with your actual S3 bucket name.

### Step 2: Deploy the Stack

Deploy the packaged template to AWS:

```bash
aws cloudformation deploy \
  --template-file packaged-template.yaml \
  --stack-name my-serverless-app \
  --capabilities CAPABILITY_IAM
```

**Parameters:**
- `--stack-name`: Name of your CloudFormation stack
- `--capabilities CAPABILITY_IAM`: Required for IAM resource creation

## Configuration

### Environment Variables

Each Lambda function is configured with the following environment variables:

- `DYNAMODB_TABLE`: DynamoDB table name for the respective function

### IAM Permissions

The application automatically creates the necessary IAM roles and policies:
- DynamoDB CRUD permissions for each table
- CloudWatch Logs permissions for Lambda functions

## API Endpoints

After deployment, the following endpoints will be available:

### Feedback Collection API
- **Type**: HTTP API
- **Endpoint**: `https://{api-id}.execute-api.{region}.amazonaws.com/Prod/`
- **Methods**: ANY
- **Purpose**: Collect and store feedback data

### Alias Prompts API
- **Type**: REST API
- **Endpoint**: `https://{api-id}.execute-api.{region}.amazonaws.com/Prod/`
- **Methods**: ANY
- **Purpose**: Retrieve alias prompts

### Usage Update API
- **Type**: REST API
- **Endpoint**: `https://{api-id}.execute-api.{region}.amazonaws.com/Prod/`
- **Methods**: ANY
- **Purpose**: Update usage statistics

## Outputs

The CloudFormation stack provides the following outputs:

- DynamoDB table names
- Lambda function ARNs
- API Gateway endpoint URLs

## Local Development

### Prerequisites
- AWS SAM CLI installed
- Docker (for local Lambda execution)


## Project Structure

```
.
├── lambdas/
│   ├── feedback_collection/
│   │   └── index.py
│   ├── get_alias_promt/
│   │   └── index.py
│   └── updateusage/
│       └── index.py
├── template.yaml
├── packaged-template.yaml
└── README.md
```

## Monitoring and Logs

- **CloudWatch Logs**: Each Lambda function automatically creates log groups
- **DynamoDB Metrics**: Monitor table performance in CloudWatch
- **API Gateway Metrics**: Track API usage and performance

## Cleanup

To remove all resources:

```bash
aws cloudformation delete-stack --stack-name my-serverless-app
```

## Security Considerations

- All API endpoints are publicly accessible
- Consider adding authentication/authorization as needed
- DynamoDB tables use pay-per-request billing mode
- IAM roles follow the principle of least privilege


### Logs

Check CloudWatch Logs for detailed error information:
- `/aws/lambda/feedback_collection`
- `/aws/lambda/get_alias_promt`
- `/aws/lambda/updateusage`

## Screenshots

![Google](https://docs.google.com/document/d/1TR_4AMgYNhvO1dI3CWUC8BB0PNZ8IKzHAj6C45wTlsI/edit?usp=sharing)


