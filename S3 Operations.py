import boto3
import os
import botocore
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--Bucket', help='Name of S3 bucket where file will go', required=True)
parser.add_argument('-f', '--File', help='Name of file that will go into the bucket', required=True)
args = parser.parse_args()

my_bucket_name = args.Bucket
my_file_name = args.File

os.environ["AWS_SHARED_CREDENTIALS_FILE"] = 'C:/My Desktop/Projects/Python/ScratchPad36/boto3user_credentials.txt'

s3 = boto3.resource('s3')

def access_all_buckets():
    try:
        for bucket in s3.buckets.all():
            for key in bucket.objects.all():
                print('bucket : ' + str(bucket) + ' object : ' + str(key.key))
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = e.response['Error']['Code']
        if error_code == '404':
            exists = False
            print('bucket does not exists')
        else:
            print(e)

def access_bucket(bucket_name):
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.all():
        body = obj.get()['Body'].read()
        print(body)

def download_file_from_bucket(bucket_name,file_name):
    try:
        s3 = boto3.client('s3')
        print('downloading file ' + file_name + ' from bucket ' + bucket_name)
        s3.download_file(bucket_name, file_name, file_name)
        print('File downloaded successfully')
    except Exception as e:
        print(e)

def upload_file_to_bucket(bucket_name,file_name):
    try:
        s3 = boto3.client('s3')
        print('uploading file ' + file_name + ' to bucket ' + bucket_name)
        s3.upload_file(file_name,bucket_name,file_name)
        print('File uploaded successfully')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    #access_all_buckets()
    #access_bucket('subhasisbucket')
    download_file_from_bucket('subhasisbucket','credentials.txt')
    #upload_file_to_bucket('subhasisbucket2', 'credentials.txt')

