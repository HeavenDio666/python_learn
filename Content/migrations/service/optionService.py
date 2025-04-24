import json
import uuid

from django.http import JsonResponse
from Content.models import Option

def option_list_service(request):
    data = json.load(request)
    _pageSize = data['pageSize']
    _currentPage = data['currentPage']
    _name = data.get('name', '')
    list = Option.objects.filter(deleted=0)
    if _name is not None and _name != '':
        list = Option.objects.filter(deleted=0, name__contains=_name)
    _list = []
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['content'] = item.content
        rest['description'] = item.description
        rest['image'] = item.image
        if item.createDate is not None:
            rest['createDate'] = item.createDate.strftime('%Y-%m-%d')
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
            "page": page
        }
    }
    return JsonResponse(data1)


def option_add_service(request):
    data = json.load(request)
    Option.objects.create(
        uid=uuid.uuid4(),
        name=data['name'],
        content=data.get('content', ''),
        description=data.get('description', ''),
        image=data.get('image'),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def option_modify_service(request):
    data = json.load(request)
    _uid = data['uid']
    _id = data['id']
    rest = Option.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Option.objects.filter(id=_id).update(
        name=data['name'],
        content=data.get('content', ''),
        description=data.get('description', ''),
        image=data.get('image'),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def option_delete_service(request):
    data = json.load(request)
    _uid = data['uid']
    _id = data['id']
    rest = Option.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Option.objects.filter(id=_id).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def option_detail_service(request):
    data = json.load(request)
    _uid = data['uid']
    item = Option.objects.filter(uid=_uid, deleted=0).first()
    if item is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    rest = {}
    rest['id'] = item.id
    rest['uid'] = item.uid
    rest['name'] = item.name
    rest['content'] = item.content
    rest['description'] = item.description
    rest['image'] = item.image
    if item.createDate is not None:
        rest['createDate'] = item.createDate.strftime('%Y-%m-%d')
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": rest
    }
    return JsonResponse(data1)
