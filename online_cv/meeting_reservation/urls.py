from django.urls import path
from . import views


urlpatterns = [
    path('meeting-reservation-list/', views.meeting_reservation_list, name='meeting_reservation_list'),
    path('meeting-reservation/create-meeting-reservation/<int:cv_user_id>/', views.create_meeting_reservation, name='create_meeting_reservation'),
]