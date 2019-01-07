import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

client = boto3.client('s3')

result= client.list_objects(Bucket='sentinel-s1-l1c', Prefix='GRD/2017/11/1/EW/DH/S1A_EW_GRDH_1SDH_20171101T114426_20171101T114536_019071_02041F_C51E/manifest.safe', RequestPayer='requester')
for o in result['Contents']:
    print(o['Key'])
    s3.Object('aabms3', o['Key']).copy_from(CopySource={'Bucket': 'sentinel-s1-l1c', 'Key': o['Key']}, RequestPayer='requester')