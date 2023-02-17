from django.http import HttpResponse


def home(requesr):
    return HttpResponse('homepage')