from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('CVs/', views.cv_list, name='cvs'),

]
