
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .API.YutNoLees import YutNoLee
from django.shortcuts import render
from django.views import templates

import datetime
import json

@csrf_exempt
def index(request):
    context = {}
    return render(request, 'YutNoLee/index.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def make_YutNoLee(request):
    YutNoLee_api = YutNoLee()
    board = YutNoLee_api.generate_YutNoLee()
    result = {
        'board' : board
    }
    return JsonResponse(result)