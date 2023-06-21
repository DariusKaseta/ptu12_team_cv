from django.urls import path
from . import views


urlpatterns = [
    path('meeting-reservation-list/', views.meeting_reservation_list, name='meeting_reservation_list'),
    path('meeting-reservation/create-meeting-reservation/<int:cv_user_id>/', views.create_meeting_reservation, name='create_meeting_reservation'),
    path('meeting-reservation/delete-meeting/<int:meeting_id>/', views.delete_meeting, name='delete_meeting'),
    path('meeting-reservation/update-meeting/<int:meeting_id>/', views.update_meeting, name='update_meeting'),
]