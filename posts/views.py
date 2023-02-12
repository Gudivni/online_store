from django.shortcuts import HttpResponse
import datetime

# Create your views here.


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    if request.method == 'GET':
        return HttpResponse(html)


def good_bye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')

