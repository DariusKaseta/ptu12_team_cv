from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from ptu12_cv.models import CV
from .forms import CvForm
from . forms import ProfileUpdateForm, UserUpdateForm


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
    if request.method == 'GET':
        form = CvForm()
        return render(request, 'user_profile/create_cv.html', {'form':form})
    elif request.method == 'POST':
        form = CvForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            cv.save()
            return redirect('cv_details', pk=cv.pk)
    
    return render(request, 'user_profile/create_cv.html', {'form':form})



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
    
    if request.method == "POST":
        form = CvForm(request.POST, request.FILES, isinstance=cv)
        if form.is_valid():
            form.save()
            return redirect('cv_details', pk=cv.pk)
    else:
        form = CvForm(instance=cv)
    return render(request, 'user_profile/update_cv.html', {'form': form})
