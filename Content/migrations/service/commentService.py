import json
import uuid
from django.http import JsonResponse

from Content.migrations.service import userService
from Content.models import User, Content, Collect, Comment


def comment_list_service(request):
    data = json.load(request)
    _pageSize = data['pageSize']
    _currentPage = data['currentPage']
    _name = data.get('name', '')
    contentList = Content.objects.filter(deleted=0)
    _content_list = []
    _dict = {}

    userList = User.objects.filter(role='1', deleted=0)
    _user_list = []
    _user_score_list = []
    _user_dict = {}

    for item in userList:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        _user_dict[item.id] = item.name
        _user_list.append(item.name)

    for item in contentList:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['image'] = item.image
        _content_list.append(item.name)
        _dict[item.uid] = item.name

    list = Comment.objects.filter(deleted=0)
    _list = []
    _comment_dict = {}
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['content'] = item.content
        _content = Content.objects.filter(uid=item.content).first()
        rest['user'] = item.user
        _user = User.objects.filter(uid=item.user).first()
        rest['userName'] = _user.name
        rest['userImage'] = _user.image
        rest['contentName'] = _content.name
        if _name != '' and _name not in _content.name:
            continue
        rest['image'] = _content.image
        rest['comment'] = item.comment
        rest['score'] = item.score
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


def comment_add_service(request):
    data = json.load(request)
    _user = userService.getCurrentUser(request)
    _content = data['content'],
    Comment.objects.create(
        uid=uuid.uuid4(),
        content=data.get('content', ''),
        comment=data.get('comment', ''),
        score=data.get('score', 0),
        user=_user.uid,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def comment_modify_service(request):
    data = json.load(request)
    _user = userService.getCurrentUser(request)
    _uid = data['uid']
    _id = data['id']
    rest = Comment.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Comment.objects.filter(id=_id).update(
        content=data.get('content', ''),
        user=_user.id,
        description=data.get('description', ''),
        price=data.get('price', ''),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def comment_delete_service(request):
    data = json.load(request)
    _id = data['id']
    _uid = data['uid']
    rest = Comment.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Comment.objects.filter(id=_id).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def comment_detail_service(request):
    data = json.load(request)
    _uid = data['uid']
    item = Comment.objects.filter(uid=_uid, deleted=0).first()
    if item is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    rest = {'id': item.id, 'uid': item.uid, 'name': item.name, 'user': item.user, 'image': item.image,
            'description': item.description}
    if item.createDate is not None:
        rest['createDate'] = item.createDate.strftime('%Y-%m-%d')
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": {
            "product": rest,
        }
    }
    return JsonResponse(data1)
