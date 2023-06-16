from django.urls import path
from . import views
# from .views import cv_participles_view


urlpatterns = [
    path("", views.index, name="index"),
    path("cv/<int:pk>/", views.cv_detail, name="cv_details"),
    path("participle/", views.cv_participles_view, name="participle_view"),
]
