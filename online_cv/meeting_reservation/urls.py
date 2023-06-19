from django.urls import path
from . import views


urlpatterns = [
    path('meeting-reservation-list/', views.meeting_reservation_list, name='meeting_reservation_list'),
    path('create-meeting-reservation/', views.create_meeting_reservation, name='create_meeting_reservation'),
]