#pages/views.py
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello World from Django, hosted on Fly.io")

