# This is an example of how to upload to the S3 bucket

import boto3
import os
from dotenv import load_dotenv

# Loading .env
load_dotenv()

# Replace 'YOUR_ACCESS_KEY' and 'YOUR_SECRET_KEY' with your AWS credentials
aws_access_key = os.getenv('aws_access_key')
aws_secret_key = os.getenv('aws_secret_key')

# Replace 'your-bucket-name' with the name of your S3 bucket
bucket_name = 'pep2-group1-etl-endpoint'

# Replace 'your-file-key' with the key under which you want to store the file in the bucket
file_key = 'test-file'

# Replace 'path/to/your/local/file.txt' with the path to the file you want to upload
current_dir = os.getcwd()
local_file_path = current_dir + '/test.txt'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Upload the file to the S3 bucket
with open(local_file_path, 'rb') as data:
    s3.put_object(Body=data, Bucket=bucket_name, Key=file_key)

print(f"File {file_key} uploaded to {bucket_name}")