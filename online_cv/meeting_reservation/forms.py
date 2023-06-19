from django import forms
from .models import MeetingReservation


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class MeetingReservationForm(forms.ModelForm):
    class Meta:
        model = MeetingReservation
        fields = ('user', 'hr_representative', 'start_time', 'end_time')
        widgets = {
            'start_time': DateTimeInput(),
            'end_time': DateTimeInput(),
        }