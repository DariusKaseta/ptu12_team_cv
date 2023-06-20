from django.urls import path
from . import views
from .views import my_cv, create_cv, update_cv


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('my-cv/', my_cv, name='my_cv'),
    path('create-cv/', create_cv, name='create_cv'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('CVs/update/', views.update_cv, name='update_cv'),
    
]
