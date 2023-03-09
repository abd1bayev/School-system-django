from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import ProfileForm

# def profile(request):
#     profile = UserProfile.objects.get(id=request.user.id)
#     context = {
#         'profile': profile
#     }
#     return render(request, 'account/profile.html', context)


def profile(request):
    try:
        profile = UserProfile.objects.get(id=request.user.id)
    except ObjectDoesNotExist:
        # handle the error in some way, e.g. redirect to a different page
        return render(request, 'account/profile_error.html')
    context = {
        'profile': profile
    }
    return render(request, 'account/profile.html', context)


# def update_profile(request):
#     profile = UserProfile.objects.get(id=request.user.id)
#     forms = ProfileForm(instance=profile)
#     if request.method == 'POST':
#         forms = ProfileForm(request.POST, request.FILES, instance=profile)
#         if forms.is_valid():
#             forms.save()
#     context = {
#         'forms': forms
#     }
#     return render(request, 'account/update-profile.html', context)

def update_profile(request):
    try:
        profile = UserProfile.objects.get(id=request.user.id)
    except UserProfile.DoesNotExist:
        # handle the error by displaying an appropriate message to the user
        return render(request, 'account/profile_error.html')

    forms = ProfileForm(instance=profile)
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=profile)
        if forms.is_valid():
            forms.save()
    context = {
        'forms': forms
    }
    return render(request, 'account/update-profile.html', context)
