from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import CV


def index(request):
    return render(request, "ptu12_cv/index.html" )


def base_view(request):
    return render(request, 'ptu12_cv/base.html')


def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    return render(request, "ptu12_cv/cv_details.html", {"cv": cv})


def cv_participles_view(request):
    participles = CV.objects.all()
    return render(request, 'ptu12_cv/cv_participles_view.html', {"participles": participles})