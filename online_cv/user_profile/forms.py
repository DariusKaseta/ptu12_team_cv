from django.contrib.auth import get_user_model
from django import forms
from . import models
from ptu12_cv.models import CV, Skill, Education, WorkExperience
from django.forms import inlineformset_factory
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget




class CvForm(forms.ModelForm):
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='LT'))
    picture = forms.ImageField(required=False)

    class Meta:
        model = CV
        fields = ("user", "title", "first_name", "last_name", "email", "phone_number", "city", "picture", "scope", "about_user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['phone_number'].required = True
        self.fields['city'].required = True
        self.fields['picture'].required = True
        self.fields['scope'].required = True
        self.fields["about_user"].required = True

    
    def save(self, commit=True):
        cv = super().save(commit=commit)
        return cv


EducationFormSet = inlineformset_factory(
    CV,
    Education,
    fields=('program', 'date_from', 'date_until', 'school', 'school_name', 'degree'),
    extra=1,
    widgets={
        'date_from': forms.DateInput(attrs={'type': 'date'}),
        'date_until': forms.DateInput(attrs={'type': 'date'}),
    }
)

WorkExperienceFormSet = inlineformset_factory(
    CV,
    WorkExperience,
    fields=('workplace_name', 'date_from', 'date_until', 'duties'),
    extra=1,
    widgets={
        'date_from': forms.DateInput(attrs={'type': 'date'}),
        'date_until': forms.DateInput(attrs={'type': 'date'}),
    }
)
SkillFormSet = inlineformset_factory(
    CV,
    Skill,
    fields=('skill',),
    extra=1
)


User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ("picture",)
