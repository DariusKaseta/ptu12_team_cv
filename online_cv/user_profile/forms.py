from django.contrib.auth import get_user_model
from django import forms
from . import models
from ptu12_cv.models import CV, Skill, Summary, Education, WorkExperience




class CvForm(forms.ModelForm):
    education_program = forms.CharField(label=("Program"), max_length=100)
    education_date_from = forms.DateField(label=("Date From"), widget=forms.DateInput(attrs={'type': 'date'}))
    education_date_until = forms.DateField(label=("Date Until"), widget=forms.DateInput(attrs={'type': 'date'}))
    education_school = forms.ChoiceField(label=("School"), choices=Education.SCHOOL_CHOICES)
    education_school_name = forms.CharField(label=("School Name"), max_length=100)
    education_degree = forms.CharField(label=("Degree"), max_length=100, initial="---")

    work_experience_workplace_name = forms.CharField(label=("Workplace Name"), max_length=100)
    work_experience_date_from = forms.DateField(label=("Date From"), widget=forms.DateInput(attrs={'type': 'date'}))
    work_experience_date_until = forms.DateField(label=("Date Until"), widget=forms.DateInput(attrs={'type': 'date'}))
    work_experience_duties = forms.CharField(label=("Duties"), max_length=100)

    skill = forms.CharField(label=("Skill"), max_length=100)

    summary_about_user = forms.CharField(label=("About User"), max_length=500, widget=forms.Textarea)

    class Meta:
        model = CV
        fields = ("user", "title", "first_name", "last_name", "email", "phone_number", "city", "picture", "scope")

    def save(self, commit=True):
        cv = super().save(commit=commit)

        education_program = self.cleaned_data['education_program']
        education_date_from = self.cleaned_data['education_date_from']
        education_date_until = self.cleaned_data['education_date_until']
        education_school = self.cleaned_data['education_school']
        education_school_name = self.cleaned_data['education_school_name']
        education_degree = self.cleaned_data['education_degree']
        education = Education(cv=cv, program=education_program, date_from=education_date_from, date_until=education_date_until, school=education_school, school_name=education_school_name, degree=education_degree)
        education.save()

        work_experience_workplace_name = self.cleaned_data['work_experience_workplace_name']
        work_experience_date_from = self.cleaned_data['work_experience_date_from']
        work_experience_date_until = self.cleaned_data['work_experience_date_until']
        work_experience_duties = self.cleaned_data['work_experience_duties']
        work_experience = WorkExperience(cv=cv, workplace_name=work_experience_workplace_name, date_from=work_experience_date_from, date_until=work_experience_date_until, duties=work_experience_duties)
        work_experience.save()

        skill = self.cleaned_data['skill']
        skill = Skill(cv=cv, skill=skill)
        skill.save()

        summary_about_user = self.cleaned_data['summary_about_user']
        summary = Summary(cv=cv, about_user=summary_about_user)
        summary.save()

        return cv
