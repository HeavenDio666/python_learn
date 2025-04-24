import json
import uuid

from django.http import JsonResponse

from Content.migrations.utils import generate
from Content.models import Test, Content, Option


def test_list_service(request):
    data = json.load(request)
    _pageSize = data['pageSize']
    _currentPage = data['currentPage']
    _name = data.get('name', '')
    list = Test.objects.filter(deleted=0)
    if _name is not None and _name != '':
        list = Test.objects.filter(deleted=0, name__contains=_name)
    _list = []
    index = 1
    typeList = [
        {
            "value": "0",
            "label": "单选题"
        },
        {
            "value": "1",
            "label": "多选题"
        },
        {
            "value": "2",
            "label": "判断题"
        }
    ]
    typeMap = {
        "0": "单选题",
        "1": "多选题",
        "2": "判断题",
    }
    for item in list:
        rest = {}
        optionList = Option.objects.filter(test=item.uid)
        for option in optionList:
            if option.choice == 'A':
                rest['optionA'] = option.name
            if option.choice == 'B':
                rest['optionB'] = option.name
            if option.choice == 'C':
                rest['optionC'] = option.name
            if option.choice == 'D':
                rest['optionD'] = option.name
            if option.choice == 'E':
                rest['optionE'] = option.name
        rest['id'] = item.id
        rest['uid'] = item.uid
        rest['name'] = item.name
        rest['analysis'] = item.analysis
        rest['type'] = item.type
        if item.type is not None and item.type != '':
            rest['typeName'] = typeMap[item.type]
        rest['answer'] = item.answer
        rest['image'] = item.image
        if item.createDate is not None:
            rest['createDate'] = item.createDate.strftime('%Y-%m-%d')
        _list.append(rest)
        index = index + 1
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
            "typeList": typeList,
            "page": page
        }
    }
    return JsonResponse(data1)


def test_add_service(request):
    data = json.load(request)
    _name = data.get('name', '')
    _content = data.get('content', '')
    _type = data.get('type', '')
    _uuid = uuid.uuid4()
    Test.objects.create(
        uid=_uuid,
        name=data['name'],
        analysis=data.get('analysis', ''),
        answer=data.get('answer', ''),
        type=data.get('type', ''),
        image=data.get('image'),
    )
    _option_list = []
    _optionA = data.get('optionA', '')
    _optionB = data.get('optionB', '')
    _optionC = data.get('optionC', '')
    _optionD = data.get('optionD', '')
    _optionE = data.get('optionE', '')
    if _optionA is not None and _optionA != '':
        Option.objects.create(
            uid=uuid.uuid4(),
            name=_optionA,
            choice='A',
            seq=1,
            test=_uuid,
        )
    if _optionB is not None and _optionB != '':
        Option.objects.create(
            uid=uuid.uuid4(),
            name=_optionB,
            choice='B',
            seq=2,
            test=_uuid,
        )
    if _optionC is not None and _optionC != '':
        Option.objects.create(
            uid=uuid.uuid4(),
            name=_optionC,
            choice='C',
            seq=3,
            test=_uuid,
        )
    if _optionD is not None and _optionD != '':
        Option.objects.create(
            uid=uuid.uuid4(),
            name=_optionD,
            choice='D',
            seq=4,
            test=_uuid,
        )
    if _optionE is not None and _optionE != '':
        Option.objects.create(
            uid=uuid.uuid4(),
            name=_optionE,
            choice='E',
            seq=5,
            test=_uuid,
        )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def test_modify_service(request):
    data = json.load(request)
    _uid = data['uid']
    _id = data['id']
    rest = Test.objects.filter(id=_id, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Test.objects.filter(id=_id).update(
        name=data['name'],
        analysis=data.get('analysis', ''),
        answer=data.get('answer', ''),
        type=data.get('type', ''),
        image=data.get('image'),
    )
    _uuid = rest.uid
    Option.objects.filter(test=_uuid).update(
        deleted=1,
    )
    _option_list = []
    _optionA = data.get('optionA', '')
    _optionB = data.get('optionB', '')
    _optionC = data.get('optionC', '')
    _optionD = data.get('optionD', '')
    _optionE = data.get('optionE', '')
    if _optionA is not None and _optionA != '':
        Option.objects.create(
            uid=uuid.uuid4(),
            name=_optionA,
            choice='A',
            seq=1,
            test=_uuid,
        )
    if _optionB is not None and _optionB != '':
        Option.objects.create(
            uid=uuid.uuid4(),
            name=_optionB,
            choice='B',
            seq=2,
            test=_uuid,
        )
    if _optionC is not None and _optionC != '':
        Option.objects.create(
            uid=uuid.uuid4(),
            name=_optionC,
            choice='C',
            seq=3,
            test=_uuid,
        )
    if _optionD is not None and _optionD != '':
        Option.objects.create(
            uid=uuid.uuid4(),
            name=_optionD,
            choice='D',
            seq=4,
            test=_uuid,
        )
    if _optionE is not None and _optionE != '':
        Option.objects.create(
            uid=uuid.uuid4(),
            name=_optionE,
            choice='E',
            seq=5,
            test=_uuid,
        )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def test_delete_service(request):
    data = json.load(request)
    _uid = data['uid']
    _id = data['id']
    rest = Test.objects.filter(uid=_uid, deleted=0).first()
    if rest is None:
        data1 = {
            "success": "false",
            "message": "查询不存在",
            "returnCode": "500",
            "returnData": data
        }
        return JsonResponse(data1)
    Test.objects.filter(id=_id).update(
        deleted=1,
    )
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": data
    }
    return JsonResponse(data1)


def test_detail_service(request):
    data = json.load(request)
    _uid = data['uid']
    item = Test.objects.filter(uid=_uid, deleted=0).first()
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
    rest['analysis'] = item.analysis
    rest['answer'] = item.answer
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


def test_generate_service(request):
    data = json.load(request)
    _amount = data.get('amount', 1)
    _content = data.get('content', "关于人工智能")
    _type = data.get('type', '0')
    generate.generate(_content, _amount, _type)
    data1 = {
        "success": "true",
        "message": "操作成功",
        "returnCode": "200",
        "returnData": _content
    }
    return JsonResponse(data1)
