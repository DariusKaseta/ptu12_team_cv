from django.shortcuts import render, redirect
from .models import MeetingReservation
from .forms import MeetingReservationForm
from .forms import MeetingReservationForm
from django.contrib.auth.decorators import login_required


def meeting_reservation_list(request):
    reservations = MeetingReservation.objects.all()
    return render(request, 'meeting_reservation/meeting_reservation_list.html', {'reservations': reservations, 'user': request.user})

@login_required
def create_meeting_reservation(request):
    if request.method == 'POST':
        form = MeetingReservationForm(request.user, request.POST)
        if form.is_valid():
            meeting_reservation = form.save(commit=False)
            meeting_reservation.user = request.user
            meeting_reservation.save()
            return redirect('meeting_reservation_list')
    else:
        form = MeetingReservationForm(request.user)
    return render(request, 'meeting_reservation/create_meeting_reservation.html', {'form': form})