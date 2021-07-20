import json

from django.http import HttpResponse, JsonResponse


# Create your views here.

def welcome(request):
    return HttpResponse('Hello world from django')


def contact(request):
    return JsonResponse({'email': 'test9@gmail.com',
                         'name': 'Fernando Colmenarez',
                         'cellphone': '99999'})
