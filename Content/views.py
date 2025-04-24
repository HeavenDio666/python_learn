from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Content.COSUploadUtils import upload_service
from Content.migrations.service import userService, contentService, \
    imageService, testService, answerService, optionService, recordService, examService, noticeService, linkService, \
    resultService, commentService, collectService


@csrf_exempt
def image_upload(request):
    return upload_service(request)


@csrf_exempt
@require_http_methods(["POST"])
def image_upload_base64(request):
    return imageService.image_upload_base64(request)


# Create your views here.
@csrf_exempt
def validate(request):
    return userService.validate_service(request)


@csrf_exempt
def register(request):
    return userService.register_service(request)


@csrf_exempt
def user_list(request):
    return userService.user_list_service(request)


@csrf_exempt
def user_add(request):
    return userService.user_add_service(request)


@csrf_exempt
def user_modify(request):
    return userService.user_modify_service(request)


@csrf_exempt
def user_delete(request):
    return userService.user_delete_service(request)


def user_detail(request):
    return userService.user_detail_service(request)


@csrf_exempt
def user_currentUser(request):
    return userService.user_currentUser_service(request)

@csrf_exempt
def content_list(request):
    return contentService.content_list_service(request)

@csrf_exempt
def content_add(request):
    return contentService.content_add_service(request)


@csrf_exempt
def content_modify(request):
    return contentService.content_modify_service(request)


@csrf_exempt
def content_delete(request):
    return contentService.content_delete_service(request)

@csrf_exempt
def content_detail(request):
    return contentService.content_detail_service(request)


@csrf_exempt
def exam_list(request):
    return examService.exam_list_service(request)

@csrf_exempt
def exam_list1(request):
    return examService.exam_list_service1(request)

@csrf_exempt
def exam_add(request):
    return examService.exam_add_service(request)


@csrf_exempt
def exam_modify(request):
    return examService.exam_modify_service(request)


@csrf_exempt
def exam_delete(request):
    return examService.exam_delete_service(request)

@csrf_exempt
def exam_detail(request):
    return examService.exam_detail_service(request)


@csrf_exempt
def test_list(request):
    return testService.test_list_service(request)

@csrf_exempt
def test_add(request):
    return testService.test_add_service(request)


@csrf_exempt
def test_modify(request):
    return testService.test_modify_service(request)


@csrf_exempt
def test_delete(request):
    return testService.test_delete_service(request)

@csrf_exempt
def test_detail(request):
    return testService.test_detail_service(request)

@csrf_exempt
def test_generate(request):
    return testService.test_generate_service(request)

@csrf_exempt
def answer_list(request):
    return answerService.answer_list_service(request)

@csrf_exempt
def answer_add(request):
    return answerService.answer_add_service(request)


@csrf_exempt
def answer_modify(request):
    return answerService.answer_modify_service(request)


@csrf_exempt
def answer_delete(request):
    return answerService.answer_delete_service(request)

@csrf_exempt
def answer_detail(request):
    return answerService.answer_detail_service(request)

@csrf_exempt
def option_list(request):
    return optionService.option_list_service(request)

@csrf_exempt
def option_add(request):
    return optionService.option_add_service(request)


@csrf_exempt
def option_modify(request):
    return optionService.option_modify_service(request)


@csrf_exempt
def option_delete(request):
    return optionService.option_delete_service(request)

@csrf_exempt
def option_detail(request):
    return optionService.option_detail_service(request)

@csrf_exempt
def record_list(request):
    return recordService.record_list_service(request)

@csrf_exempt
def record_add(request):
    return recordService.record_add_service(request)


@csrf_exempt
def record_modify(request):
    return recordService.record_modify_service(request)


@csrf_exempt
def record_delete(request):
    return recordService.record_delete_service(request)

@csrf_exempt
def record_detail(request):
    return recordService.record_detail_service(request)


@csrf_exempt
def notice_list(request):
    return noticeService.notice_list_service(request)

@csrf_exempt
def notice_add(request):
    return noticeService.notice_add_service(request)


@csrf_exempt
def notice_modify(request):
    return noticeService.notice_modify_service(request)


@csrf_exempt
def notice_delete(request):
    return noticeService.notice_delete_service(request)

@csrf_exempt
def notice_detail(request):
    return noticeService.notice_detail_service(request)

@csrf_exempt
def result_list(request):
    return resultService.result_list_service(request)

@csrf_exempt
def result_add(request):
    return resultService.result_add_service(request)


@csrf_exempt
def result_modify(request):
    return resultService.result_modify_service(request)


@csrf_exempt
def result_delete(request):
    return resultService.result_delete_service(request)

@csrf_exempt
def result_detail(request):
    return resultService.result_detail_service(request)


@csrf_exempt
def link_list(request):
    return linkService.link_list_service(request)

@csrf_exempt
def link_add(request):
    return linkService.link_add_service(request)


@csrf_exempt
def link_modify(request):
    return linkService.link_modify_service(request)


@csrf_exempt
def link_delete(request):
    return linkService.link_delete_service(request)

@csrf_exempt
def link_detail(request):
    return linkService.link_detail_service(request)


@csrf_exempt
def collect_list(request):
    return collectService.collect_list_service(request)

@csrf_exempt
def collect_add(request):
    return collectService.collect_add_service(request)


@csrf_exempt
def collect_modify(request):
    return collectService.collect_modify_service(request)


@csrf_exempt
def collect_delete(request):
    return collectService.collect_delete_service(request)

@csrf_exempt
def collect_detail(request):
    return collectService.collect_detail_service(request)



@csrf_exempt
def comment_list(request):
    return commentService.comment_list_service(request)

@csrf_exempt
def comment_add(request):
    return commentService.comment_add_service(request)


@csrf_exempt
def comment_modify(request):
    return commentService.comment_modify_service(request)


@csrf_exempt
def comment_delete(request):
    return commentService.comment_delete_service(request)

@csrf_exempt
def comment_detail(request):
    return commentService.comment_detail_service(request)