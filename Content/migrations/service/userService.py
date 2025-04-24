import json
import uuid

from django.http import JsonResponse
from Content.models import User
import hashlib
import jwt


def validate_service(request):
    data = json.load(request)
    username = data['username']
    password = data['password']
    md5 = hashlib.md5(password.encode())  # 创建一个md5对象
    salt = "$1$asd"
    md5.update(salt.encode())
    encrypted_data = md5.hexdigest()
    _user = User.objects.filter(username=username, password=encrypted_data, deleted=0).first()
    payload = {
        "username": username
    }
    _token = jwt.encode(payload=payload, key="tk123")
    # decoded_token = _token.decode('utf-8')
    decoded_token = _token
    if _user is not None:
        rest = {}
        rest['id'] = _user.id
        rest['uid'] = _user.uid
        rest['name'] = _user.name
        rest['username'] = _user.username
        rest['gender'] = _user.gender
        rest['age'] = _user.age
        rest['role'] = _user.role
        rest['mobile'] = _user.mobile
        rest['email'] = _user.email
        rest['image'] = _user.image
        data1 = {
            "success": "true",
            "message": "请求成功",
            "returnCode": "200",
            "returnData": {
                "logintoken": decoded_token,
                "user": rest
            }
        }
        return JsonResponse(data1)
    data1 = {
        "success": "false",
        "message": "账号或者密码错误",
        "returnCode": "500",
        "returnData": ""
    }
    return JsonResponse(data1)


def register_service(request):
    data = json.load(request)
    username = data['username']
    password = data['password']
    rest = User.objects.filter(username=username, deleted=0).first()
    if rest is not None:
        data1 = {
            "success": "false",
            "message": "用户已存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    md5 = hashlib.md5(password.encode())  # 创建一个md5对象
    salt = "$1$asd"
    md5.update(salt.encode())
    encrypted_data = md5.hexdigest()
    User.objects.create(
        name=data['name'],
        username=data['username'],
        password=encrypted_data,
        mobile=data['mobile'],
        email=data['email'],
        role=data['role'],
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def user_list_service(request):
    data = json.load(request)
    _pageSize = data['pageSize']
    _currentPage = data['currentPage']
    _name = data.get('name', '')
    _mobile = data.get('mobile', '')
    _gender = data.get('gender', '')
    _role = data['role']
    list = User.objects.filter(deleted=0, role='1')
    if _name is not None and _name != '':
        list = User.objects.filter(deleted=0, name__contains=_name)
    _list = []
    genderMap = {
        "male": "男",
        "female": "女"
    }
    genderList = [
        {
            "value": "male",
            "label": "男"
        },
        {
            "value": "female",
            "label": "女"
        }
    ]
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['username'] = item.username
        rest['password'] = item.password
        rest['gender'] = item.gender
        if item.gender is not None and item.gender != '':
            if _gender not in item.gender:
                continue
        if item.gender is not None and item.gender != '':
            rest['genderName'] = genderMap[item.gender]
        rest['age'] = item.age
        rest['role'] = item.role
        if item.role is not None and item.role != '':
            if _role not in item.role:
                continue
        rest['mobile'] = item.mobile
        if item.mobile is not None and item.mobile != '':
            if _mobile not in item.mobile:
                continue
        rest['email'] = item.email
        rest['image'] = item.image
        _list.append(rest)
    page = {
        "pageSize": _pageSize,
        "total": len(_list),
        "currentPage": _currentPage
    }
    if _pageSize < len(_list):
        if _pageSize * _currentPage > len(_list):
            _start = (_currentPage - 1) * _pageSize
            _list = _list[_start: len(_list)]
        if _pageSize * _currentPage <= len(_list):
            _start = (_currentPage - 1) * _pageSize
            _end = _currentPage * _pageSize
            _list = _list[_start: _end]
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": {
            "list": _list,
            "page": page,
            "genderList": genderList
        }
    }
    return JsonResponse(data1)


def user_add_service(request):
    data = json.load(request)
    username = data['username']
    password = data['password']
    rest = User.objects.filter(username=username, deleted=0).first()
    if rest is not None:
        data1 = {
            "success": "false",
            "message": "用户已存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    md5 = hashlib.md5(password.encode())  # 创建一个md5对象
    salt = "$1$asd"
    md5.update(salt.encode())
    encrypted_data = md5.hexdigest()
    User.objects.create(
        uid=uuid.uuid4(),
        name=data['name'],
        username=data['username'],
        password=encrypted_data,
        age=data.get('age', 25),
        gender=data.get('gender', ''),
        mobile=data.get('mobile', ''),
        email=data.get('email', ''),
        role=data['role'],
        image=data.get('image', ''),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def user_modify_service(request):
    data = json.load(request)
    _uid = data['uid']
    password = data['password']
    # 字典不存在，加一个默认值
    gender = data.get('gender', "male")
    rest = User.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "用户不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    md5 = hashlib.md5(password.encode())  # 创建一个md5对象
    salt = "$1$asd"
    md5.update(salt.encode())
    encrypted_data = md5.hexdigest()
    User.objects.filter(uid=_uid).update(
        name=data['name'],
        username=data['username'],
        password=encrypted_data,
        gender=gender,
        age=data.get('age', 25),
        mobile=data.get('mobile', ''),
        email=data.get('email', ''),
        image=data.get('image', ''),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def user_delete_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = User.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "用户不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    User.objects.filter(uid=_uid).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def user_detail_service(request):
    data = json.load(request)
    _uid = data['uid']
    item = User.objects.filter(uid=_uid, deleted=0).first()
    if item is None:
        data1 = {
            "success": "false",
            "message": "用户不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    rest = {}
    rest['id'] = item.id
    rest['uid'] = item.uid
    rest['name'] = item.name
    rest['username'] = item.username
    rest['password'] = item.password
    rest['gender'] = item.gender
    rest['age'] = item.age
    rest['mobile'] = item.mobile
    rest['email'] = item.email
    rest['image'] = item.image
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": rest
    }
    return JsonResponse(data1)


def user_currentUser_service(request):
    data = json.load(request)
    item = getCurrentUser(request)
    if item is None:
        data1 = {
            "success": "false",
            "message": "用户不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    rest = {}
    rest['id'] = item.id
    rest['uid'] = item.uid
    rest['name'] = item.name
    rest['username'] = item.username
    rest['password'] = item.password
    rest['gender'] = item.gender
    rest['age'] = item.age
    rest['role'] = item.role
    rest['mobile'] = item.mobile
    rest['email'] = item.email
    rest['image'] = item.image
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": rest
    }
    return JsonResponse(data1)


def getCurrentUser(request):
    _authorization = request.META.get('HTTP_AUTHORIZATION')
    # _payload = jwt.decode(_authorization, key="tk123")
    _payload = jwt.decode(_authorization, key="tk123", algorithms='HS256')
    _username = _payload['username']
    _user = User.objects.filter(username=_username, deleted=0).first()
    return _user
