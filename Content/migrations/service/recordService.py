import datetime
import json
from django.http import JsonResponse
from Content.models import Record, User, Answer, Exam


def record_list_service(request):
    examList = Exam.objects.filter(deleted=0)
    _exam_list = []
    _dict = {}

    userList = User.objects.filter(deleted=0)
    _user_list = []
    _user_dict = {}

    for item in userList:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        _user_dict[item.uid] = item.name
        _user_list.append(item.name)

    for item in examList:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['image'] = item.image
        _exam_list.append(item.name)
        _dict[item.uid] = item.name

    statusMap = {
        0: "未提交",
        1: "已提交"
    }

    list = Record.objects.filter(status=1, deleted=0)
    _list = []
    for item in list:
        rest = {}
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['exam'] = item.exam
        if item.exam is not None and item.exam != '':
            rest['examName'] = _dict[item.exam]
        rest['user'] = item.user
        if item.user is not None and item.user != '':
            rest['userName'] = _user_dict.get(item.user, '')
        rest['score'] = item.score
        rest['status'] = item.status
        rest['statusName'] = statusMap.get(item.status, '已提交')
        rest['createDate'] = item.createDate.strftime('%Y-%m-%d')
        _list.append(rest)
    page = {
        "currentPage": 1,
        "total": len(_list)
    }
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": {
            "list": _list,
            "userList": _user_list,
            "page": page,
        }
    }
    return JsonResponse(data1)


def calculate_score(list):
    score = 0
    for item in list:
        score = score + item.score
    average = score / len(list)
    return format(average, '.2f')


def record_add_service(request):
    data = json.load(request)
    _uid = data.get('uid', '')
    record = Record.objects.filter(uid=_uid).first()
    answerList = Answer.objects.filter(record=_uid)
    _score = 0
    for item in answerList:
        if item.status == 1:
            _score = _score + 1
    Record.objects.filter(id=record.id).update(
        score=_score,
        status=1,
        endTime=datetime.datetime.now(),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def record_modify_service(request):
    data = json.load(request)
    _uid = data['uid']
    rest = Record.objects.filter(uid=_uid, deleted=0).first()
    _answer_list = Answer.objects.filter(record=rest.uid)
    score = 0
    for item in _answer_list:
        score = score + item.score
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Record.objects.filter(id=rest.id).update(
        score=score,
        status="1",
        endDate=data.get('endDate', datetime.datetime.now()),
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def record_delete_service(request):
    data = json.load(request)
    _id = data['id']
    _uid = data['uid']
    rest = Record.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Record.objects.filter(id=_id).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def record_detail_service(request):
    data = json.load(request)
    _uid = data['uid']
    item = Record.objects.filter(uid=_uid, deleted=0).first()
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
    if item.startDate is not None:
        rest['startDateName'] = item.startDate.strftime('%Y-%m-%d %H-%M-%S')
    if item.endDate is not None:
        rest['endDateName'] = item.endDate.strftime('%Y-%m-%d %H-%M-%S')
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
