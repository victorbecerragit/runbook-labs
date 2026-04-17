import boto3
def get_bedrock_runtime():
    # Helper to get the boto3 runtime client for Bedrock
    return boto3.client('bedrock-runtime')
