from django import forms
from .models import MeetingReservation

class MeetingReservationForm(forms.ModelForm):
    class Meta:
        model = MeetingReservation
        fields = ['user', 'hr_representative', 'start_time', 'end_time']