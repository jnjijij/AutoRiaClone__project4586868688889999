# backend/autoria_clone/system/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import UserProfile
from ...system.forms import UserProfileForm

User = get_user_model()

@login_required
def profile(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()
    if not user_profile:
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'system/profile.html', {'form': form})
