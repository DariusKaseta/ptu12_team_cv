from django import forms
from .models import MeetingReservation
from django.contrib.auth import get_user_model
from .models import HRRepresentative

User = get_user_model()

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class MeetingReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.cv_user = kwargs.pop("cv_user")
        self.current_user = kwargs.pop("current_user")
        super(MeetingReservationForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = self.cv_user
        self.fields['hr_representative'].queryset = HRRepresentative.objects.filter(user=self.current_user)
        self.fields['hr_representative'].initial = HRRepresentative.objects.filter(user=self.current_user).first()
        self.fields['parties'].choices = [(self.cv_user.pk, self.cv_user.get_full_name()), (self.current_user.pk, self.current_user.get_full_name())]

    class Meta:
        model = MeetingReservation
        fields = ('hr_representative', 'user', 'start_time', 'end_time', 'parties')
        widgets = {
            'user': forms.HiddenInput(),
            'start_time': DateTimeInput(),
            'end_time': DateTimeInput(),
        }
