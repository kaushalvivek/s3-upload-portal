import string
import random
import boto3
from botocore.client import Config
from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY, BUCKET_NAME, AWS_REGION

def generate_random_string(stringLength=20):
  letters = string.ascii_lowercase
  return ''.join(random.choice(letters) for i in range(stringLength))

def upload_to_s3(image):
    s3 = boto3.resource(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )
    name = generate_random_string()
    extension = image.content_type.split('/')[-1]
    try:
        s3.Bucket(BUCKET_NAME).put_object(Key=f"{name}.{extension}", Body=image)
        get_url = f"https://{BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{name}.{extension}"
        return_object = {
        'status':'SUCCESS',
        'get_url':get_url,
        }
    except Exception as e :
        return_object = {
            'status': e,
            'get_url':'',
        }

    finally:
        return return_object