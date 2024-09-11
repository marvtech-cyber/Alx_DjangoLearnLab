from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, 'blog/base.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Should be request.POST, not request.Post

        if form.is_valid():
            user = form.save()
            user.refresh_from_db() #Load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')  # Should be form.cleaned_data.get('password1'), not form.cleaned_data('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to the home page
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})