from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import CV, Education, WorkExperience, Skill, Summary
from django.db.models import Q
import pdfkit
from django.template.loader import get_template







def base_view(request):
    return render(request, 'ptu12_cv/base.html')


def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    education = Education.objects.filter(cv=cv)
    work_experience = WorkExperience.objects.filter(cv=cv)
    skill = Skill.objects.filter(cv=cv)
    summary = Summary.objects.filter(cv=cv)
    return render(
        request,
        "ptu12_cv/cv_details.html", 
        {"cv": cv, 
        "education": education, 
        "work_experience": work_experience, 
        "skill": skill,
        "summary": summary})

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

def cv_pdf_view(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    context = {'cv': cv}
    html = get_template('ptu12_cv/cv_details.html').render(context)
    # html = get_template('cv_details.html').render(context)


    pdf = pdfkit.from_string(html, False)


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    response.write(pdf)

    return response


# def cv_pdf_view(request, pk):
#     # Fetch the CV object
#     cv = get_object_or_404(CV, pk=pk)

#     # Render the cv_detail.html template with the CV object
#     context = {'cv': cv}
#     html = render(request, 'cv_details.html', context).content

#     # Generate the PDF using django-pdfkit
#     pdf = pdfkit.from_string(html, False)

#     # Create an HTTP response with PDF content for download
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
#     response.write(pdf)

#     return response

