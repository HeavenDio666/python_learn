import json
import uuid

from django.http import JsonResponse

from Content.migrations.service import userService
from Content.models import Notice, Result, User, Link


def result_list_service(request):
    data = json.load(request)
    _pageSize = data['pageSize']
    _currentPage = data['currentPage']
    # tuple
    _name = data.get('name', '')
    list = Result.objects.filter(deleted=0)
    choice_dict = {
        "A": "不感兴趣",
        "B": "略微感兴趣",
        "C": "一般感兴趣",
        "D": "比较感兴趣",
        "E": "非常感兴趣",
    }
    _list = []
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['user'] = item.user
        _user = User.objects.filter(uid=item.user).first()
        if _user is None:
            continue
        rest['userName'] = _user.name
        rest['link'] = item.link
        _link = Link.objects.filter(uid=item.link).first()
        if _link is None:
            continue
        rest['linkName'] = _link.name
        if _name != '' and _name not in _link.name:
            continue
        rest['choice'] = item.choice
        rest['choiceName'] = choice_dict.get(item.choice, '')
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
            "page": page,
        }
    }
    return JsonResponse(data1)


def result_add_service(request):
    data = json.load(request)
    _user = userService.getCurrentUser(request)
    _link = data['link']
    _result = Result.objects.filter(user=_user.uid, link=_link, deleted=0).first()
    if _result is None:
        Result.objects.create(
            uid=uuid.uuid4(),
            link=data['link'],
            choice=data.get('choice', ''),
            user=_user.uid,
        )
        data1 = {
            "success": "true",
            "message": "操作成功",
            "returnCode": "200",
            "returnData": data
        }
        return JsonResponse(data1)
    Result.objects.filter(uid=_result._uid).update(
        choice=data.get('choice', ''),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def result_modify_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = Result.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Result.objects.filter(uid=_uid).update(
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


def result_delete_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = Result.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Result.objects.filter(uid=_uid).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def result_detail_service(request):
    data = json.load(request)
    _uid = data['uid']
    item = Result.objects.filter(uid=_uid, deleted=0).first()
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
    rest['user'] = item.user
    rest['link'] = item.link
    rest['choice'] = item.choice
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": rest
    }
    return JsonResponse(data1)
