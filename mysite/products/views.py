from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Hello surbhi')


def new(request):
    return HttpResponse('New products')
