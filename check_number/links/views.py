from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse, JsonResponse

from .models import Link
from .serializers import LinksSerializer

import json
import re


class GetLinkInfoView(APIView):
    def get(self, request):
        queryset = Link.objects.all()
        serializer_for_queryset = LinksSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)


def index(request):
    return HttpResponse('К URL добавте телефонный номер, который нужно проверить')


def number(request, slug):
    slug = re.sub('^(\+7)', '8', slug)
    slug = re.sub('[^0-9]', '', slug)

    if Link.objects.filter(number=slug):
        return JsonResponse({'found': 1})
    else:
        return JsonResponse({'found': 0})

