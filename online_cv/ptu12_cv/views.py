from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import CV
from django.db.models import Q
from django.template.loader import render_to_string
import weasyprint
import pdfkit
from django.core.paginator import Paginator








def base_view(request):
    return render(request, 'ptu12_cv/base.html')


def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    # education = get_object_or_404(Education, pk=pk)
    return render(request, "ptu12_cv/cv_details.html", {"cv": cv})


def cv_participles_view(request):
    participles = CV.objects.all()
    paginator = Paginator(participles, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'ptu12_cv/cv_participles_view.html', {"participles": participles, 'page_obj': page_obj})


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




def cv_pdf_view(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)

    context = {'cv' : cv}
    html = render_to_string('ptu12_cv/cv_details_pdf.html', context)

    pdf = weasyprint.HTML(string=html).write_pdf()

    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename= cv_details.pdf'
    response.write(pdf)

    return response


def cv_participles_search(request):
    query = request.GET.get('query')
    search_results = CV.objects.filter(
        Q(first_name__icontains = query)|
        Q(last_name__icontains = query)|
        Q(email__icontains = query)|
        Q(phone_number__icontains = query)|
        Q(city__icontains = query)|
        Q(title__icontains = query)
    )
    return render(request, "includes/cv_participles_search.html", {'cvs': search_results, 'query':query})