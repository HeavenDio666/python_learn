import json
import uuid

from django.http import JsonResponse

from Content.migrations.service import userService
from Content.models import Exam, User, Content, Test, ExamTest, Option, Record


def exam_list_service(request):
    data = json.load(request)
    _pageSize = data['pageSize']
    _currentPage = data['currentPage']
    # tuple
    _name = data.get('name', '')
    list = Exam.objects.filter(deleted=0)
    _list = []
    userList = User.objects.filter(deleted=0, role='1')
    _content_list = []
    contentList = Content.objects.filter(deleted=0)
    _user_list = []
    _dict = {}
    _user_dict = {}
    for item in contentList:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        _content_list.append(rest)
        _dict[item.uid] = item.name
    for item in userList:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        _user_list.append(rest)
        _user_dict[item.id] = item.name
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['content'] = item.content
        rest['user'] = item.user
        rest['judge'] = item.judge
        rest['multiple'] = item.multiple
        rest['single'] = item.single
        if item.content is not None and item.content != '':
            rest['contentName'] = _dict[item.content]
        # if item.user is not None and item.user != '':
        #     rest['userName'] = _user_dict[item.user]
        rest['status'] = item.status
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
            "page": page,
            "contentList": _content_list,
            "userList": _user_list
        }
    }
    return JsonResponse(data1)


def exam_list_service1(request):
    data = json.load(request)
    _user = userService.getCurrentUser(request)
    _pageSize = data['pageSize']
    _currentPage = data['currentPage']
    # tuple
    _name = data.get('name', ''),
    list = Exam.objects.filter(deleted=0, status='1')
    _list = []
    userList = User.objects.filter(deleted=0, role='1')
    _content_list = []
    contentList = Content.objects.filter(deleted=0)
    _user_list = []
    _dict = {}
    _user_dict = {}
    for item in contentList:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        _content_list.append(rest)
        _dict[item.uid] = item.name
    for item in userList:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        _user_list.append(rest)
        _user_dict[item.id] = item.name
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['content'] = item.content
        rest['user'] = item.user
        rest['judge'] = item.judge
        rest['multiple'] = item.multiple
        rest['single'] = item.single
        if item.content is not None and item.content != '':
            rest['contentName'] = _dict[item.content]
        # if item.user is not None and item.user != '':
        #     rest['userName'] = _user_dict[item.user]
        rest['status'] = item.status
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
            "page": page,
            "contentList": _content_list,
            "userList": _user_list
        }
    }
    return JsonResponse(data1)


def exam_add_service(request):
    data = json.load(request)
    _user = userService.getCurrentUser(request)
    _judge_num = data.get('judge', 0),
    _multiple_num = data.get('multiple', 0),
    _single_num = data.get('single', 0),
    _uuid = uuid.uuid4()
    Exam.objects.create(
        uid=_uuid,
        name=data['name'],
        content=data.get('content', ''),
        judge=data.get('judge', 0),
        multiple=data.get('multiple', 0),
        single=data.get('single', 0),
        user=_user.id,
        description=data.get('description', ''),
        image=data.get('image'),
    )
    singleList = Test.objects.filter(type='0')
    multipleList = Test.objects.filter(type='1')
    judgeList = Test.objects.filter(type='2')
    _seq = 1
    _single = 0
    for item in singleList:
        if int(_single_num[0]) < _single:
            break
        ExamTest.objects.create(
            exam=_uuid,
            test=item.uid,
            seq=_seq,
        )
        _single = _single + 1
        _seq = _seq + 1
    _multiple = 0
    for item in multipleList:
        if int(_multiple_num[0]) < _multiple:
            break
        ExamTest.objects.create(
            exam=_uuid,
            test=item.uid,
            seq=_seq,
        )
        _multiple = _multiple + 1
        _seq = _seq + 1
    _judge = 0
    for item in judgeList:
        if int(_judge_num[0]) < _judge:
            break
        ExamTest.objects.create(
            exam=_uuid,
            test=item.uid,
            seq=_seq,
        )
        _judge = _judge + 1
        _seq = _seq + 1
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def exam_modify_service(request):
    _user = userService.getCurrentUser(request)
    data = json.load(request)
    _uid = data['uid']
    rest = Exam.objects.filter(uid=_uid, deleted=0).first()
    _judge_num = data.get('judge', 0),
    _multiple_num = data.get('multiple', 0),
    _single_num = data.get('single', 0),
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    _uuid = rest.uid
    Exam.objects.filter(uid=_uid).update(
        name=data['name'],
        content=data.get('content', ''),
        judge=data.get('judge', 0),
        multiple=data.get('multiple', 0),
        single=data.get('single', 0),
        status=data.get('status', ''),
        user=data.get('user', _user.id),
        description=data.get('description', ''),
        image=data.get('image'),
    )
    ExamTest.objects.filter(exam=_uuid).delete()
    singleList = Test.objects.filter(type='0')
    multipleList = Test.objects.filter(type='1')
    judgeList = Test.objects.filter(type='2')
    _seq = 1
    _single = 0
    for item in singleList:
        if int(_single_num[0]) < _single:
            break
        ExamTest.objects.create(
            exam=_uuid,
            test=item.uid,
            seq=_seq,
        )
        _single = _single + 1
        _seq = _seq + 1
    _multiple = 0
    for item in multipleList:
        if int(_multiple_num[0]) < _multiple:
            break
        ExamTest.objects.create(
            exam=_uuid,
            test=item.uid,
            seq=_seq,
        )
        _multiple = _multiple + 1
        _seq = _seq + 1
    _judge = 0
    for item in judgeList:
        if int(_judge_num[0]) < _judge:
            break
        ExamTest.objects.create(
            exam=_uuid,
            test=item.uid,
            seq=_seq,
        )
        _judge = _judge + 1
        _seq = _seq + 1
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def exam_delete_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = Exam.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Exam.objects.filter(uid=_uid).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def exam_detail_service(request):
    data = json.load(request)
    _uid = data['uid']
    item = Exam.objects.filter(uid=_uid, deleted=0).first()
    if item is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    _user = userService.getCurrentUser(request)
    record = Record.objects.filter(user=_user.uid, exam=_uid, status=0).first()
    _record = uuid.uuid4()
    if record is not None:
        _record = record.uid
    if record is None:
        Record.objects.create(
            uid=_record,
            user=_user.uid,
            exam=_uid,
            status='0'
        )
    rest = {}
    rest['id'] = item.id
    rest['uid'] = item.uid
    rest['name'] = item.name
    rest['content'] = item.content
    rest['judge'] = item.judge
    rest['multiple'] = item.multiple
    rest['single'] = item.single
    rest['status'] = item.status
    rest['user'] = item.user
    userList = User.objects.filter(deleted=0)
    _user_list = []
    _user_dict = {}
    for _item in userList:
        _rest = {}
        _rest['id'] = _item.id
        _rest['uid'] = _item.uid
        _rest['name'] = _item.name
        _user_list.append(_rest)
        _user_dict[_item.uid] = _item.name
    if item.user is not None and item.user != '':
        rest['userName'] = _user_dict.get(item.user, '')
    _content_list = []
    contentList = Content.objects.filter(deleted=0)
    _dict = {}
    for content in contentList:
        _rest = {}
        _rest['id'] = content.id
        _rest['uid'] = content.uid
        _rest['name'] = content.name
        _content_list.append(_rest)
        _dict[content.uid] = content.name
    if item.content is not None and item.content != '':
        rest['contentName'] = _dict.get(item.content, '')
    rest['description'] = item.description
    rest['image'] = item.image
    _single_list = []
    _multiple_list = []
    _judge_list = []
    examList = ExamTest.objects.filter(exam=_uid)
    _exam_dict = {}
    for exam in examList:
        _exam_dict[exam.test] = exam.exam
    testList = Test.objects.filter(deleted=0)
    _test_dict = {}
    for test in testList:
        _rest = {}
        _rest['id'] = test.id
        _rest['uid'] = test.uid
        _rest['name'] = test.name
        _rest['type'] = test.type
        _rest['multipleSelection'] = []
        _exam = _exam_dict.get(test.uid, '')
        if _exam is None or _exam == '':
            continue
        optionList = Option.objects.filter(test=test.uid)
        _option_list = []
        for option in optionList:
            _option = {}
            _option['id'] = option.id
            _option['uid'] = option.uid
            _option['choice'] = option.choice
            _option['name'] = option.name
            _option_list.append(_option)
        _rest['optionList'] = _option_list
        if _rest['type'] == '0':
            _single_list.append(_rest)
        if _rest['type'] == '1':
            _multiple_list.append(_rest)
        if _rest['type'] == '2':
            _judge_list.append(_rest)
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": {
            "rest": rest,
            "record": _record,
            "singleList": _single_list,
            "multipleList": _multiple_list,
            "judgeList": _judge_list,
            "single": len(_single_list),
            "multiple": len(_multiple_list),
            "judge": len(_judge_list),
        }
    }
    return JsonResponse(data1)
