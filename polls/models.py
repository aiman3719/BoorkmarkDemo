import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


    was_published_recently.admin_order_field = 'pub_date'     # 원칙적으로 임의의메서드에 의한 값은 정렬이 불가한데, 다른으로 정렬.
    was_published_recently.boolean = True    # 값이 boolean값 형태인지 설정합니다.
    was_published_recently.shot_description = 'Published recently'   # 항목의 헤더이름을 설정합니다.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text




