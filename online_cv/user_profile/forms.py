from django.contrib.auth import get_user_model
from django import forms
from . import models
from ptu12_cv.models import CV, Skill, Education, WorkExperience
from django.forms import formset_factory, inlineformset_factory


EducationFormSet = inlineformset_factory(
    CV,
    Education,
    fields=('program', 'date_from', 'date_until', 'school', 'school_name', 'degree'),
    extra=1,
    can_delete=True
)
WorkExperienceFormSet = inlineformset_factory(
    CV,
    WorkExperience,
    fields=('workplace_name', 'date_from', 'date_until', 'duties'),
    extra=1,
    can_delete=True
)
SkillFormSet = inlineformset_factory(
    CV,
    Skill,
    fields=('skill',),
    extra=1,
    can_delete=True
)



class CvForm(forms.ModelForm):

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
        # self.fields['picture'].required = True
        self.fields['scope'].required = True
        self.fields["about_user"].required = True



    def save(self, commit=True):
        cv = super().save(commit=commit)

        if commit:
            education_program = self.cleaned_data['education_program']
            education_date_from = self.cleaned_data['education_date_from']
            education_date_until = self.cleaned_data['education_date_until']
            education_school = self.cleaned_data['education_school']
            education_school_name = self.cleaned_data['education_school_name']
            education_degree = self.cleaned_data['education_degree']
            education = Education(
                cv=cv, 
                user=cv.user,
                program=education_program, 
                date_from=education_date_from, 
                date_until=education_date_until, 
                school=education_school, 
                school_name=education_school_name, 
                degree=education_degree)
            education.save()

            work_experience_workplace_name = self.cleaned_data['work_experience_workplace_name']
            work_experience_date_from = self.cleaned_data['work_experience_date_from']
            work_experience_date_until = self.cleaned_data['work_experience_date_until']
            work_experience_duties = self.cleaned_data['work_experience_duties']
            work_experience = WorkExperience(
                cv=cv, 
                user=cv.user,
                workplace_name=work_experience_workplace_name, 
                date_from=work_experience_date_from, 
                date_until=work_experience_date_until, 
                duties=work_experience_duties)
            work_experience.save()

            skill_set_skill = self.cleaned_data['skillset_skill']
            skill_set = Skill(
                cv=cv, 
                user=cv.user,
                skill=skill_set_skill)
            skill_set.save()
        return cv



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
