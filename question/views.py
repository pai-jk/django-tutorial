from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from question.models import Question


# Create your views here.
def hello_world(request):
    print("git_test")
    return HttpResponse('hello_world')


@csrf_exempt
def question_create(requset):
    """Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.
    """
    question_text = requset.POST.get('question_text')
    question = Question.objects.create(question_text=question_text)
    question.save()
    return HttpResponse(200)


def question_read(requset):
    """Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.
    """
    question_id = '외부에서 사용자가 보낸 id 값'
    question = 'question_id로 가져온 question 인스턴스 값'
    return 'question의 __str__()를 이용해 출력되는 문자열'


def question_update(requset):
    """Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.
    """
    question_id = '외부에서 사용자가 보낸 id 값'
    answer = '외부에서 사용자가 보낸 answer 값'
    question = 'question_id로 가져온 question 인스턴스 값'
    "question 의 answer을 입력받은 값으로 update"
    return 'question의 __str__()를 이용해 출력되는 문자열'


def question_delete(requset):
    """Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.
    """
    question_id = '외부에서 사용자가 보낸 id 값'
    question = 'question_id로 가져온 question 인스턴스 값'
    "question 인스턴스를 삭제한다 ."

    if "question_id로 인스턴스 조회시 없으면 ":
        return HttpResponse(200)
    else:
        return HttpResponse(400)
