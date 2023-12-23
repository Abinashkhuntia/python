import boto3
import requests

def download_to_s3(url, bucket, key):
    s3 = boto3.resource('s3')
    response = requests.get(url)
    s3.Bucket(bucket).put_object(Key=key, Body=response.content)

# Usage
url = 'https://file-examples.com/wp-content/storage/2017/02/file-sample_100kB.doc'
bucket = 'newasdfa'
key = 'DSA/file-sample_100kB.doc'
download_to_s3(url, bucket, key)