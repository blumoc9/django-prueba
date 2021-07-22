import json

from django.http import HttpResponse, JsonResponse


# Create your views here.

def welcome(request):
    return HttpResponse('Welcome to django world')


def contact(request):
    return JsonResponse({'email': 'test9@gmail.com',
                         'name': 'Fernando Colmenarez',
                         'cellphone': '99999'})
