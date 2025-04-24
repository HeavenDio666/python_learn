"""subscribe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from Content import views

urlpatterns = [
    path("rest/user/validate", views.validate),
    path("rest/user/register", views.register),
    path("rest/user/list", views.user_list),
    path("rest/user/add", views.user_add),
    path("rest/user/modify", views.user_modify),
    path("rest/user/delete", views.user_delete),
    path("rest/user/detail", views.user_detail),
    path("rest/user/currentUser", views.user_currentUser),
    path("rest/image/upload", views.image_upload),
    path("rest/image/uploadBase64", views.image_upload_base64),

    path("rest/content/list", views.content_list),
    path("rest/content/add", views.content_add),
    path("rest/content/modify", views.content_modify),
    path("rest/content/delete", views.content_delete),
    path("rest/content/detail", views.content_detail),

    path("rest/notice/list", views.notice_list),
    path("rest/notice/add", views.notice_add),
    path("rest/notice/modify", views.notice_modify),
    path("rest/notice/delete", views.notice_delete),
    path("rest/notice/detail", views.notice_detail),

    path("rest/exam/list", views.exam_list),
    path("rest/exam/list1", views.exam_list1),
    path("rest/exam/add", views.exam_add),
    path("rest/exam/modify", views.exam_modify),
    path("rest/exam/delete", views.exam_delete),
    path("rest/exam/detail", views.exam_detail),

    path("rest/test/list", views.test_list),
    path("rest/test/add", views.test_add),
    path("rest/test/modify", views.test_modify),
    path("rest/test/delete", views.test_delete),
    path("rest/test/detail", views.test_detail),
    path("rest/test/generate", views.test_generate),

    path("rest/record/list", views.record_list),
    path("rest/record/add", views.record_add),
    path("rest/record/modify", views.record_modify),
    path("rest/record/delete", views.record_delete),
    path("rest/record/detail", views.record_detail),

    path("rest/option/list", views.option_list),
    path("rest/option/add", views.option_add),
    path("rest/option/modify", views.option_modify),
    path("rest/option/delete", views.option_delete),
    path("rest/option/detail", views.option_detail),

    path("rest/answer/list", views.answer_list),
    path("rest/answer/add", views.answer_add),
    path("rest/answer/modify", views.answer_modify),
    path("rest/answer/delete", views.answer_delete),
    path("rest/answer/detail", views.answer_detail),

    path("rest/link/list", views.link_list),
    path("rest/link/add", views.link_add),
    path("rest/link/modify", views.link_modify),
    path("rest/link/delete", views.link_delete),
    path("rest/link/detail", views.link_detail),

    path("rest/result/list", views.result_list),
    path("rest/result/add", views.result_add),
    path("rest/result/modify", views.result_modify),
    path("rest/result/delete", views.result_delete),
    path("rest/result/detail", views.result_detail),

    path("rest/collect/list", views.collect_list),
    path("rest/collect/add", views.collect_add),
    path("rest/collect/modify", views.collect_modify),
    path("rest/collect/delete", views.collect_delete),
    path("rest/collect/detail", views.collect_detail),

    path("rest/comment/list", views.comment_list),
    path("rest/comment/add", views.comment_add),
    path("rest/comment/modify", views.comment_modify),
    path("rest/comment/delete", views.comment_delete),
    path("rest/comment/detail", views.comment_detail),
]
