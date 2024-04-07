from django.shortcuts import render,redirect
from .models import Profile
from .forms import ProfileForm
# Create your views here.
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

def view_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('movieprofile:edit_profile')
    return render(request, 'view.html', {'profile': profile})

def edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
         profile = Profile(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('movieprofile:view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit1.html', {'form': form})