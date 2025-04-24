import json
import uuid

from django.http import JsonResponse
from Content.models import Content, User, Collect, Comment


def content_list_service(request):
    data = json.load(request)
    _pageSize = data['pageSize']
    _currentPage = data['currentPage']
    # tuple
    _name = data.get('name', ''),
    list = Content.objects.filter(deleted=0)
    # if _name is not None and _name != '':
    #     list = Content.objects.filter(deleted=0, name__contains=_name)
    _list = []
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['period'] = item.period
        rest['author'] = item.author
        rest['video'] = item.video
        rest['score'] = calculate_score(item.uid)
        rest['price'] = item.price
        rest['content'] = item.content
        rest['description'] = item.description
        rest['image'] = item.image
        if item.createDate is not None:
            rest['createDate'] = item.createDate.strftime('%Y-%m-%d')
        _list.append(rest)
    _list.sort(key=lambda x: x['score'], reverse=True)
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
        }
    }
    return JsonResponse(data1)

def calculate_score(content):
    collectList = Collect.objects.filter(content=content)
    commentList = Comment.objects.filter(content=content)
    return len(collectList) + len(commentList)

def content_add_service(request):
    data = json.load(request)
    Content.objects.create(
        uid=uuid.uuid4(),
        name=data['name'],
        period=data.get('period', ''),
        author=data.get('author', ''),
        video=data.get('video', ''),
        price=data.get('price', ''),
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


def content_modify_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = Content.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Content.objects.filter(uid=_uid).update(
        name=data['name'],
        period=data.get('period', ''),
        author=data.get('author', ''),
        video=data.get('video', ''),
        price=data.get('price', ''),
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


def content_delete_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = Content.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Content.objects.filter(uid=_uid).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def content_detail_service(request):
    data = json.load(request)
    _uid = data['uid']
    item = Content.objects.filter(uid=_uid, deleted=0).first()
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
    rest['period'] = item.period
    rest['author'] = item.author
    rest['video'] = item.video
    rest['price'] = item.price
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
