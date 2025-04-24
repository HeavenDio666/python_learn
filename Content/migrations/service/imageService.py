import base64
import logging
import random
import sys

from django.http import JsonResponse
from qcloud_cos import CosConfig, CosS3Client


def image_upload_base64(request):
    image = request.POST.get('image')
    uid = request.POST.get('uid')
    prefix = 'data:image/png;base64,'
    _image = image.replace(prefix, '')
    _bytes = base64.b64decode(_image)
    _name = "snapshots" + generate_random_string(10)
    _key = "/image/" + _name
    # 正常情况日志级别使用 INFO，需要定位时可以修改为 DEBUG，此时 SDK 会打印和服务端的通信信息
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    # 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在 CosConfig 中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
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


def generate_random_string(randomlength):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


if __name__ == '__main__':
    print(generate_random_string(10))
