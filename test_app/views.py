from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("test 2")
    dic = {'test_var':'Test using injection from Django - Index'}
    return render(request, 'test_app/index.html', context=dic)

def help(request):
    dic = {'help_var': 'Test using injection from Django - Help'}
    return render(request, 'test_app/help.html', context=dic)

