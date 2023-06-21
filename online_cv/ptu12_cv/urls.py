from django.urls import path
from . import views
# from .views import cv_pdf_view, cv_participles_view



urlpatterns = [
    path("", views.index, name="index"),
    path('CVs/', views.cv_list, name='cvs'),
    path("cv/<int:pk>/", views.cv_detail, name="cv_details"),
    path("participle/", views.cv_participles_view, name="participle_view"),
    # path('cv/<int:cv_id>/generate-pdf/', views.cv_pdf_view, name='cv_details_pdf'),
    # path('CVs/update/', views.update_cv, name='update_cv'),
    path('cv/<int:cv_id>/generate-pdf/', views.cv_pdf_view, name='cv_details_pdf'),


    


]
