from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render, get_object_or_404


User = get_user_model()

@login_required
def profile(request, user_id=None):
    if user_id == None:
        user = request.user
    else:
        user = get_object_or_404(get_user_model(), id=user_id)
    return render(request, 'user_profile/profile.html', {'user_': user})
