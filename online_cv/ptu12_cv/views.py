from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import CV
from django.db.models import Q
from django.template.loader import render_to_string
import weasyprint
import pdfkit








def base_view(request):
    return render(request, 'ptu12_cv/base.html')


def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    # education = get_object_or_404(Education, pk=pk)
    return render(request, "ptu12_cv/cv_details.html", {"cv": cv})


def cv_participles_view(request):
    participles = CV.objects.all()
    return render(request, 'ptu12_cv/cv_participles_view.html', {"participles": participles})

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


