from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "ptu12_cv/index.html" )


def base_view(request):
    return render(request, 'ptu12_cv/base.html')