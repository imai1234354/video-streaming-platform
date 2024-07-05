import json
import boto3

def lambda_handler(event, context):
    # S3バケットとオブジェクトキーを取得
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # AWS MediaConvertクライアントを作成
    mediaconvert = boto3.client('mediaconvert', endpoint_url='https://<mediaconvert-endpoint>')
    
    # メディアコンバートジョブの作成
    job_settings = {
        "Inputs": [{
            "FileInput": f"s3://{bucket}/{key}"
        }],
        "OutputGroups": [{
            "Name": "File Group",
            "OutputGroupSettings": {
                "Type": "FILE_GROUP_SETTINGS",
                "FileGroupSettings": {
                    "Destination": f"s3://{bucket}/outputs/"
                }
            },
            "Outputs": [{
                "Preset": "System-Ott_Hls_Ts_Avc_Aac_16x9_1280x720p_24Hz_3.5Mbps"
            }]
        }]
    }
    
    # メディアコンバートジョブの送信
    response = mediaconvert.create_job(
        JobTemplate='my-job-template',
        Role='arn:aws:iam::123456789012:role/MediaConvert_Default_Role',
        Settings=job_settings
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('MediaConvert job started successfully')
    }
