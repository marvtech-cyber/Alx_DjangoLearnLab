from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name="register"),
    path('profile/', views.profile_view, name = 'profile'),
     path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/edit/', views.edit_profile_view, name = 'profile_edit'),
]