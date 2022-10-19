#pages/views.py
from django.http import HttpResponse
from django.template import loader


def homePageView(request):
    template = loader.get_template('pages/index.html')
    return HttpResponse(template.render({}, request))

