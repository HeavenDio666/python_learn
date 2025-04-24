import uuid
from django.db import models


class User(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    role = models.CharField(max_length=64)
    image = models.CharField(max_length=1024)
    age = models.IntegerField()
    mobile = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_user'


class Content(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    name = models.CharField(max_length=64)
    period = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024)
    video = models.CharField(max_length=1024)
    price = models.CharField(max_length=1024)
    content = models.CharField(max_length=1024)
    image = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_content'

class Notice(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=1024)
    content = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_notice'


class Score(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    content = models.CharField(max_length=64)
    score = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.CharField(max_length=1024)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_score'


class Exam(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    name = models.CharField(max_length=64)
    content = models.CharField(max_length=1024)
    image = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    status = models.CharField(max_length=1024)
    user = models.CharField(max_length=1024)
    single = models.IntegerField(default=0)
    multiple = models.IntegerField(default=0)
    judge = models.IntegerField(default=0)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        db_table = 'python_learn_exam'


class Test(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    name = models.CharField(max_length=64)
    analysis = models.CharField(max_length=64)
    answer = models.CharField(max_length=64)
    image = models.CharField(max_length=1024)
    type = models.CharField(max_length=64)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_test'


class Option(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    test = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    choice = models.CharField(max_length=64)
    seq = models.IntegerField(default=0)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_option'

class ExamTest(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    exam = models.CharField(max_length=64)
    test = models.CharField(max_length=64)
    seq = models.IntegerField(default=0)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_exam_test'

class Answer(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    record = models.CharField(max_length=64)
    exam = models.CharField(max_length=64)
    test = models.CharField(max_length=64)
    answer = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)
    user = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_answer'

class Record(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    exam = models.CharField(max_length=64)
    user = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    score = models.DecimalField(max_digits=10, decimal_places=2)
    startTime = models.DateField(auto_now_add=True)
    endTime = models.DateField(auto_now_add=True)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_exam_record'


class Link(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=64)
    seq = models.IntegerField(default=0)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_link'

class Result(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    user = models.CharField(max_length=64)
    link = models.CharField(max_length=64)
    choice = models.CharField(max_length=64)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_result'

class Comment(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    user = models.CharField(max_length=64)
    content = models.CharField(max_length=1024)
    comment = models.CharField(max_length=1024)
    score = models.IntegerField(default=0)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_comment'

class Collect(models.Model):
    uid = models.CharField(max_length=64, default=uuid.uuid4())
    user = models.CharField(max_length=64)
    content = models.CharField(max_length=1024)
    deleted = models.IntegerField(default=0)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    operator = models.CharField(max_length=64)

    class Meta:
        ordering = ['createDate']
        db_table = 'python_learn_collect'