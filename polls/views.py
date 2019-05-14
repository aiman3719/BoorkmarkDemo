from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    tempate = loader.get_template('polls//index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }

    return HttpResponse(tempate.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def result(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

