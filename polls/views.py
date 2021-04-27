from collections import defaultdict

from django.shortcuts import render


# Create your views here.
from polls.models import Choice, Question


def index(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return render(request, 'polls/index.html', context)
