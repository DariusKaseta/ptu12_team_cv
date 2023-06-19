from django.shortcuts import render, redirect
from .models import MeetingReservation
from .forms import MeetingReservationForm


def meeting_reservation_list(request):
    reservations = MeetingReservation.objects.all()
    return render(request, 'meeting_reservation/meeting_reservation_list.html', {'reservations': reservations})

def create_meeting_reservation(request):
    if request.method == 'POST':
        form = MeetingReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meeting_reservation/meeting_reservation_list')
    else:
        form = MeetingReservationForm()
    return render(request, 'meeting_reservation/create_meeting_reservation.html', {'form': form})
