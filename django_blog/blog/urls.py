from django.urls import path, include
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name="register"),
    path('profile/', views.profile_view, name = 'profile'),
    path('profile/edit/', views.edit_profile_view, name = 'profile_edit'),
]