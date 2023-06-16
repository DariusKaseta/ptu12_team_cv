from django.http import HttpResponse
from django.shortcuts import render
from . models import CV
from django.db.models import Q




def base_view(request):
    return render(request, 'ptu12_cv/base.html')

def index(request):

    num_cvs = CV.objects.all().count()

    context = {
        'num_cvs' : num_cvs
    }

    return render(request, "ptu12_cv/index.html", context=context )

def cv_list(request):
    qs = CV.objects.all()
    query = request.GET.get('query')
    if query:
        qs = qs.filter(
            Q(title__icontains=query)|
            Q(first_name__icontains=query)|
            Q(last_name__icontains=query)|
            Q(email__icontains=query)|
            Q(phone__icontains=query)|
            Q(city__icontains=query)
        )

   
    return render(request, 'ptu12_cv/cvs.html', {'cv_list': qs,
    })