from django import forms
from django_countries.fields import CountryField
from .models import CV

class Cvform(forms.ModelForms):
    country_code = CountryField().formfield()

    class Meta:
        model = CV
        fields = ['user', 'first_name', 'last_name', 'email'  'phone_number', 'country_code', 'city', 'picture', 'title', 'scope']