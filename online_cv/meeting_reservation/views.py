from django.shortcuts import render, redirect
from .models import MeetingReservation
from .forms import MeetingReservationForm
from .models import HRRepresentative
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def meeting_reservation_list(request):
    reservations = MeetingReservation.objects.all()
    return render(request, 'meeting_reservation/meeting_reservation_list.html', {'reservations': reservations})

def create_meeting_reservation(request, cv_user_id):
    cv_user = get_object_or_404(User, id=cv_user_id)
    
    if request.method == 'POST':
        form = MeetingReservationForm(request.POST, current_user=request.user, cv_user=cv_user)
        if form.is_valid():
            meeting_reservation = form.save(commit=False)
            hr_representative = get_object_or_404(HRRepresentative, user=request.user)
            meeting_reservation.hr_representative = hr_representative
            meeting_reservation.save()
            meeting_reservation.parties.add(cv_user)
            meeting_reservation.parties.add(hr_representative.user)
            meeting_reservation.save()

            return redirect('meeting_reservation_list')
    else:
        form = MeetingReservationForm(current_user=request.user, cv_user=cv_user)
    
    return render(request, 'meeting_reservation/create_meeting_reservation.html', {'form': form, 'cv_user': cv_user})

def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(MeetingReservation, id=meeting_id)
    if request.method == 'POST':
        meeting.delete()
        return redirect('meeting_reservation_list')
    return render(request, 'meeting_reservation/delete_meeting.html', {'meeting': meeting})

def update_meeting(request, meeting_id):
    meeting = get_object_or_404(MeetingReservation, id=meeting_id)
    if request.method == 'POST':
        form = MeetingReservationForm(request.POST, instance=meeting, cv_user=meeting.user, current_user=request.user)
        if form.is_valid():
            form.save()
            return redirect('meeting_reservation_list')
    else:
        form = MeetingReservationForm(instance=meeting, cv_user=meeting.user, current_user=request.user)
    return render(request, 'meeting_reservation/update_meeting.html', {'form': form})