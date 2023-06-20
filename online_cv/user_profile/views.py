from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from ptu12_cv.models import CV, Education, WorkExperience, Skill, Summary
from .forms import CvForm
from .forms import ProfileUpdateForm, UserUpdateForm, EducationFormSet, WorkExperienceFormSet, SkillFormSet, SummaryFormSet
from django.forms import inlineformset_factory
from django.http import HttpResponseBadRequest


User = get_user_model()


@login_required
def profile(request, user_id=None):
    if user_id == None:
        user = request.user
    else:
        user = get_object_or_404(get_user_model(), id=user_id)
    return render(request, 'user_profile/profile.html', {'user_': user})

@csrf_protect
def signup(request):
    if request.user.is_authenticated:
        messages.info(request, 'In order to sign up, you need to logout first')
        return redirect('index')
    if request.method == "POST":
        error = False
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if not username or len(username) < 3 or User.objects.filter(username=username).exists():
            error = True
            messages.error(request, 'Username is too short or already exists.')
        if not email or len(email) < 3 or User.objects.filter(email=email).exists():
            error = True
            messages.error(request, 'Email is invalid or user with this email already exists.')
        if not password or not password_confirm or password != password_confirm or len(password) < 8:
            error = True
            messages.error(request, "Password must be at least 8 characters long and match.")
        if not error:
            user = User.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            user.set_password(password)
            user.save()
            messages.success(request, "User registration successful!")
            return redirect('login')
    return render(request, 'user_profile/signup.html')


@login_required
def my_cv(request):
    user_cv = CV.objects.filter(user=request.user)
    return render(request, 'user_profile/my_cv.html', {'user_cv':user_cv})


@login_required
def create_cv(request):
    form = CvForm()
    education_formset = EducationFormSet(instance=CV(), prefix='education_formset')
    work_experience_formset = WorkExperienceFormSet(instance=CV(), prefix='work_experience_formset')
    skill_formset = SkillFormSet(instance=CV(), prefix='skill_formset')
    
    if request.method == 'POST':
        form = CvForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            
            education_formset = EducationFormSet(request.POST, instance=cv, prefix = 'education_formset')
            work_experience_formset = WorkExperienceFormSet(request.POST, instance=cv, prefix = 'work_experience_formset')
            skill_formset = SkillFormSet(request.POST, instance=cv, prefix= 'skill_formset' )

            if education_formset.is_valid() and work_experience_formset.is_valid() and skill_formset.is_valid():
                cv.save()

                for education_form in education_formset:
                    education_form.instance.user = request.user

                for work_experience_form in work_experience_formset:
                    work_experience_form.instance.user = request.user

                for skill_form in skill_formset:
                    skill_form.instance.user = request.user

                education_formset.save()
                work_experience_formset.save()
                skill_formset.save()

                return redirect('cv_details', pk=cv.pk)
    
    else:
        form = CvForm()
        education_formset = EducationFormSet(instance=CV(), prefix='education_formset')
        work_experience_formset = WorkExperienceFormSet(instance=CV(), prefix='work_experience_formset')
        skill_formset = SkillFormSet(instance=CV(), prefix='skill_formset')

    return render(
        request,
        'user_profile/create_cv.html',
        {
            'form':form,
            'education_formset':education_formset,
            'work_experience_formset':work_experience_formset,
            'skill_formset':skill_formset,
        }
    )


@login_required
@csrf_protect
def profile_update(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'user_profile/profile_update.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def update_cv(request):
    cv_id = request.GET.get("cv_id")
    cv = get_object_or_404(CV, pk=cv_id, user=request.user)
    EducationFormSet = inlineformset_factory(CV, Education, fields=('program', 'date_from', 'date_until', 'school', 'school_name', 'degree'), extra=0, can_delete=True)
    WorkExperienceFormSet = inlineformset_factory(CV, WorkExperience, fields=('workplace_name', 'date_from', 'date_until', 'duties'), extra=0, can_delete=True)
    SkillFormSet = inlineformset_factory(CV, Skill, fields=('skill',), extra=0, can_delete=True)
    SummaryFormSet = inlineformset_factory(CV, Summary, fields=("about_user",), extra=0, can_delete=True)
    
    if request.method == "POST":
        form = CvForm(request.POST, request.FILES, instance=cv)
        education_formset = EducationFormSet(request.POST, prefix='education', instance=cv)
        work_experience_formset = WorkExperienceFormSet(request.POST, prefix='work_experience', instance=cv)
        skill_formset = SkillFormSet(request.POST, prefix='skill', instance=cv)
        summary_formset = SummaryFormSet(request.POST, prefix='summary', instance=cv)
        
        if form.is_valid() and education_formset.is_valid() and work_experience_formset.is_valid() and skill_formset.is_valid() and summary_formset.is_valid():
            cv = form.save()
            education_formset.instance = cv
            work_experience_formset.instance = cv
            skill_formset.instance = cv
            summary_formset.instance = cv

            education_formset.save()
            work_experience_formset.save()
            skill_formset.save()
            summary_formset.save()
            
            return redirect('cv_details', pk=cv.pk)
        else:
            print(form.errors)
            print(education_formset.errors)
            print(work_experience_formset.errors)
            print(skill_formset.errors)
            print(summary_formset.errors)
            return HttpResponseBadRequest("Couldn't update form, try again.")
    
    else:
        form = CvForm(instance=cv)
        education_formset = EducationFormSet(prefix='education', instance=cv)
        work_experience_formset = WorkExperienceFormSet(prefix='work_experience', instance=cv)
        skill_formset = SkillFormSet(prefix='skill', instance=cv)
        summary_formset = SummaryFormSet(prefix='summary', instance=cv)
    
    return render(request, 'user_profile/update_cv.html', {
        'form': form,
        "education_formset": education_formset,
        "work_experience_formset": work_experience_formset,
        "skill_formset": skill_formset,
        "summary_formset": summary_formset
    })

    




