from django import forms
from .models import MeetingReservation


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class MeetingReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MeetingReservationForm, self).__init__(*args, **kwargs)
        # # self.fields['hr_representative'].widget = forms.HiddenInput()
        # self.fields['hr_representative'].disabled = True

    class Meta:
        model = MeetingReservation
        fields = ('user', 'hr_representative', 'start_time', 'end_time', 'parties')
        widgets = {
            'start_time': DateTimeInput(),
            'end_time': DateTimeInput(),
        }