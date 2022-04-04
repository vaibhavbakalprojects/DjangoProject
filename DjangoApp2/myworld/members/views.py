from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from members.models import Members
# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def showallmembers(request):
    template = loader.get_template('index.html')
    members = Members.objects.all().values()
    output = ""
    for x in members:
        output += x["firstname"]

    return HttpResponse(output)


class SubClass:
    def index2(request):
        template = loader.get_template('index2.html')
        return HttpResponse(template.render())
