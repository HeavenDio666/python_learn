import datetime
import json
import uuid

from django.http import JsonResponse

from Content.migrations.service import userService
from Content.models import Answer, User, Content, Record, Test


def answer_list_service(request):
    data = json.load(request)
    _pageSize = data['pageSize']
    _currentPage = data['currentPage']
    _content = data.get('content', '')
    _user = userService.getCurrentUser(request)
    list = Answer.objects.filter(deleted=0)
    if _user.role == '1':
        list = Answer.objects.filter(deleted=0, user=_user.uid)
    _list = []
    _status_dict = {
        "0": "比对失败",
        "1": "比对成功"
    }
    contentList = Content.objects.filter(deleted=0)
    _content_list = []
    _dict = {}
    for item in contentList:
        rest = {}
        rest['uid'] = item.uid
        rest['name'] = item.name
        _content_list.append(rest)
        _dict[item.uid] = item.name
    userList = User.objects.filter(deleted=0, role='1')
    _user_list = []
    _user_dict = {}
    _user_image_dict = {}
    for item in userList:
        rest = {}
        rest['uid'] = item.uid
        rest['name'] = item.name
        _user_list.append(rest)
        _user_dict[item.uid] = item.name
        _user_image_dict[item.uid] = item.image
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['score'] = item.score
        rest['image'] = item.image
        rest['content'] = item.content
        if item.content is not None and item.content != '':
            rest['contentName'] = _dict.get(item.content, '')
        rest['status'] = item.status
        if item.status is not None and item.status != '':
            rest['statusName'] = _status_dict.get(item.status, '')
        rest['user'] = item.user
        if item.user is not None and item.user != '':
            rest['userName'] = _user_dict.get(item.user, '')
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
            "contentList": _content_list,
            "userList": _user_list,
        }
    }
    return JsonResponse(data1)


def answer_add_service(request):
    data = json.load(request)
    _exam = data.get('exam', '')
    _answer = data.get('answer', '')
    _test = data.get('test', '')
    _record = data.get('record', '')
    _user = userService.getCurrentUser(request)
    _score = 0
    answer = Answer.objects.filter(record=_record, test=_test).first()
    test = Test.objects.filter(uid=_test).first()
    _status = "0"
    if test.answer == _answer:
        _status = 1
    if answer is not None:
        Answer.objects.filter(id=answer.id).update(
            answer=_answer,
            status=_status,
        )
    if answer is None:
        Answer.objects.create(
            uid=uuid.uuid4(),
            user=_user.uid,
            exam=_exam,
            record=_record,
            test=_test,
            answer=_answer,
            correct=test.answer,
            status=_status,
        )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def answer_modify_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = Answer.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Answer.objects.filter(uid=_uid).update(
        content=data.get('content', ''),
        user=data.get('user', ''),
        period=data.get('period', '0'),
        contentDate=data.get('contentDate', datetime.datetime.now()),
        status=data.get('status', '0'),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def answer_delete_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = Answer.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Answer.objects.filter(uid=_uid).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def detail_service(request):
    data = json.load(request)
    _uid = data['uid']
    item = Answer.objects.filter(uid=_uid, deleted=0).first()
    if item is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    user = User.objects.filter(deleted=0, uid=item.user).first()
    _user = {'id': user.id, 'uid': user.uid, 'name': user.name, 'username': user.username, 'password': user.password,
             'gender': user.gender, 'age': user.age, 'mobile': user.mobile, 'email': user.email, 'image': user.image}
    rest = {'id': item.id, 'uid': item.uid, 'period': item.period}
    rest['user'] = item.user
    rest['contentDate'] = item.contentDate
    if item.contentDate is not None:
        rest['contentDateName'] = item.contentDate.strftime('%Y-%m-%d')
    if item.createDate is not None:
        rest['createDate'] = item.createDate.strftime('%Y-%m-%d')
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": {
            "user": _user,
            "product": rest,
            "content": _content
        }
    }
    return JsonResponse(data1)
