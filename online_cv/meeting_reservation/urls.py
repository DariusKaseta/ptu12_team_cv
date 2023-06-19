from django.urls import path
from . import views

urlpatterns = [
    path('meeting-reservations/', views.meeting_reservation_list, name='meeting_reservation_list'),
    path('meeting-reservations/create/', views.create_meeting_reservation, name='create_meeting_reservation'),
]