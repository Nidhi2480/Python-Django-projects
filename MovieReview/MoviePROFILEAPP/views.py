from django.shortcuts import render,redirect
from .models import Profile
from .forms import ProfileForm
# Create your views here.
def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'view.html', {'profile': profile})

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('movieprofile:view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit1.html', {'form': form})