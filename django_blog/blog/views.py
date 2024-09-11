from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

@login_required
def profile_view(request):
    user = request.user
    profile = Profile.objects.get_or_create(user=user)[0]
    return render(request, 'blog/profile.html', {'profile': profile})

@login_required
def edit_profile_view(request):
    user = request.user
    profile = Profile.objects.get_or_create(user=user)[0]
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'blog/edit_profile.html', {'form': form})

class PostListView(ListView):
    "a class based view to display all blog posts."
    model = Post
    template_name = 'blog/posts_lists.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_url'] = 'post_delete'
        return context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'post_update'
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = '/post_list/'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    success_url = '/blog/post_list'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/post_list'
