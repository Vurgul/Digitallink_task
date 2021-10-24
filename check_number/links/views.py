from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Link

import json

import re


def index(request):
    return HttpResponse('К URL добавте телефонный номер, который нужно проверить')


def number(request, slug):
    slug = re.sub('^(\+7)', '8', slug)
    slug = re.sub('[^0-9]', '', slug)

    if Link.objects.filter(number=slug):
        return JsonResponse({'found': 1})
    else:
        return JsonResponse({'found': 0})

