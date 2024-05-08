import boto3
import json

s3_client = boto3.client('s3')

def generate_presigned_url(bucket_name, object_key, expiration_time):
    url = s3_client.generate_presigned_url(
        'put_object',
        Params={'Bucket': bucket_name, 'Key': object_key},
        ExpiresIn=expiration_time
    )
    return url

def lambda_handler(event, context):
    bucket_name = 'sharefilezz'
    object_key = event['file_name']
    expiration_time = 3600  # URL expiration time in seconds
    presigned_url = generate_presigned_url(bucket_name, object_key, expiration_time)
    return {
        'statusCode': 200,
        'body': json.dumps({'presigned_url': presigned_url})
    }
