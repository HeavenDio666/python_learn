import json
import uuid

from django.http import JsonResponse
from Content.models import Notice, Link


def link_list_service(request):
    data = json.load(request)
    _pageSize = data.get('pageSize', 10)
    _currentPage = data.get('currentPage', 1)
    # tuple
    _name = data.get('name', ''),
    list = Link.objects.filter(deleted=0)
    # if _name is not None and _name != '':
    #     list = Content.objects.filter(deleted=0, name__contains=_name)
    _option_list = [
        {
            "uid":"1",
            "choice": "A",
            "name": "不感兴趣"
        },
        {
            "uid":"2",
            "choice": "B",
            "name": "略微感兴趣"
        },
        {
            "uid": "3",
            "choice": "C",
            "name": "一般感兴趣"
        },
        {
            "uid": "4",
            "choice": "D",
            "name": "比较感兴趣"
        },
        {
            "uid": "5",
            "choice": "E",
            "name": "非常感兴趣"
        }
    ]
    _list = []
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['seq'] = item.seq
        rest['image'] = item.image
        rest['optionList'] = _option_list
        if item.createDate is not None:
            rest['createDate'] = item.createDate.strftime('%Y-%m-%d')
        _list.append(rest)
    page = {
        "pageSize": _pageSize,
        "total": len(_list),
        "currentPage": _currentPage
    }
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": {
            "list": _list,
            "page": page,
        }
    }
    return JsonResponse(data1)


def link_add_service(request):
    data = json.load(request)
    Link.objects.create(
        uid=uuid.uuid4(),
        name=data['name'],
        seq=data.get('seq', 1),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def link_modify_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = Link.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Link.objects.filter(uid=_uid).update(
        name=data['name'],
        seq=data.get('seq', 1),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def link_delete_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = Link.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Link.objects.filter(uid=_uid).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def link_detail_service(request):
    data = json.load(request)
    _uid = data['uid']
    item = Link.objects.filter(uid=_uid, deleted=0).first()
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
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": rest
    }
    return JsonResponse(data1)
