from django.contrib import admin
from . import models
from .models import CV
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget


admin.site.register(models.WorkExperience)
admin.site.register(models.Education)
admin.site.register(models.Skill)
# admin.site.register(models.CV)


class CvPhoneForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone_number': PhoneNumberPrefixWidget(initial='LT'),
        }


@admin.register(CV)
class CvAdmin(admin.ModelAdmin):
    form = CvPhoneForm