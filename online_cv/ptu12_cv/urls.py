from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from user_profile.views import my_cv




urlpatterns = [
    path("", views.index, name="index"),
    path('CVs/', views.cv_list, name='cvs'),
    path("cv/<int:pk>/", views.cv_detail, name="cv_details"),
    path("participle/", views.cv_participles_view, name="participles_view"),
    path('cv/<int:cv_id>/generate-pdf/', views.cv_pdf_view, name='cv_details_pdf'),
    path('cv_participles_search/', views.cv_participles_search, name='cv_participles_search'),
    path('delete-cv/<int:cv_id>/', views.delete_cv, name='delete-cv'),
    path('my-cv/', my_cv, name='my_my_cv'),


] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
