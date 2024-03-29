#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ref: https://github.com/thestrid3r/s3_bucketsize
"""

import boto3
from datetime import datetime, timedelta
import csv

def bucket_size(a,b):
    bucket_name = a
    cloudwatch = boto3.client('cloudwatch',
                              region_name=b)
    response = cloudwatch.get_metric_statistics(
        Namespace="AWS/S3",
        MetricName="BucketSizeBytes",
        Dimensions=[
            {
                "Name": "BucketName",
                "Value": bucket_name
            },
            {
                "Name": "StorageType",
                "Value": "StandardStorage"
            }
        ],
        StartTime=datetime.now() - timedelta(days=2),
        EndTime=datetime.now() - timedelta(days=1),
        Period=86400,
        Statistics=['Average']
    )
    #print(response)
    try:
        bucket_size_bytes = response['Datapoints'][0]['Average']
    except:
        if response['Datapoints'] == []:
            bucket_size_bytes = 0
        else:
            print("Unexpected Error")

    return '{0:.2f} GB'.format(bucket_size_bytes/1024/1024/1024)

s3api= boto3.client('s3')
resp = s3api.list_buckets()
#print (resp)
bkt_list = [x["Name"] for x in resp["Buckets"]]
#print (bkt_list)
bucket_list= {}
for x in bkt_list:
    #print (x)
    reigon_name = s3api.get_bucket_location(Bucket=x)["LocationConstraint"]
    #print (s3api.get_bucket_location(Bucket=x))
    if reigon_name is None:
        reigon_name="us-east-1"
    #print(x , reigon_name)
    bucket_list [x] = reigon_name

#bucket_list = {"name":"reigon}

with open('bucket_size'+ '_' + datetime.now().strftime('%Y-%m-%d') +'.csv' ,'w') as file:
    writer=csv.writer(file, delimiter='\t',lineterminator='\n',)
    for x in bucket_list:
        #    print(x ,"-" , bucket_size(x,bucket_list[x]))
        row = x , bucket_size(x,bucket_list[x])
        writer.writerow(row)