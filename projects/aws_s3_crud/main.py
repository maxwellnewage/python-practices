import boto3

BUCKET_NAME = '<put-your-bucket-name>'
FILE_PATH = "resources/file_1.txt"

s3 = boto3.client('s3')

# check if bucket exists, if not, create it
all_my_buckets = [bucket["Name"] for bucket in s3.list_buckets()["Buckets"]]

if BUCKET_NAME not in all_my_buckets:
    print(f'{BUCKET_NAME} bucket does not exist. Creating...')
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={'LocationConstraint': 'sa-east-1'}
    )
    print(f'{BUCKET_NAME} bucket has been created.')
else:
    print(f'{BUCKET_NAME} bucket already exists. No need to create new one.')

# upload file to s3 bucket
s3.upload_file(FILE_PATH, BUCKET_NAME, FILE_PATH)

# get file and print the text inside
file = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_PATH)["Body"].read()
print(file)

# delete the file by bucket and key
s3.delete_object(Bucket=BUCKET_NAME, Key=FILE_PATH)

# delete the bucket
s3.delete_bucket(Bucket=BUCKET_NAME)
