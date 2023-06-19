from django.urls import path
from . import views
# from views import my_cv


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    # path('profile/update/', views.profile_update, name='profile_update'),
    # path('my-cv/', my_cv, name='my_cv'),

]
