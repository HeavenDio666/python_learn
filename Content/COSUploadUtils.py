from django.http import JsonResponse
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging


def upload_service(request):
    file = request.FILES['file']
    _bytes = file.read()
    _name = file.name
    _key = "/image/" + _name
    # 正常情况日志级别使用 INFO，需要定位时可以修改为 DEBUG，此时 SDK 会打印和服务端的通信信息
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    # 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在 CosConfig 中移除，请在参数 Bucket 中带上 Appid。Bucket 由
    # BucketName-Appid 组成
    secret_id = 'AKIDqYjup5v0wd3GUbS7bryiCQQCrJkg75B0'
    secret_key = 'nV0FG2mLgvtpY2JMLAl6B1QaVAakdJj3'
    region = 'ap-nanjing'

    token = None
    scheme = 'https'

    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
    client = CosS3Client(config)
    client.put_object(
        Bucket='school-1258608700',
        Body=_bytes,
        Key=_key,
        EnableMD5=False
    )
    _image = "https://" + "school-1258608700" + ".cos." + region + ".myqcloud.com" + _key
    data1 = {
        "success": "true",
        "message": "上传成功",
        "returnCode": "200",
        "returnData": {
            "image": _image
        }
    }
    return JsonResponse(data1)
