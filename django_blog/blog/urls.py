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
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('post_detail/<pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post_create/', views.PostCreateView.as_view(), name = 'post_create'),
    path('post_update/<pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<pk>/', views.PostDeleteView.as_view(), name='post_delete'),
]