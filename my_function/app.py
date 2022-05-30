import boto3

def lambda_handler(event, context):
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

    return "There are totally {} buckets.".format(len(response['Buckets']))
