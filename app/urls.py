from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home, name="home"), 

    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name="logout"),

    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/pages/login.html"), name="login"),

    path('register/', register, name="register"),

    path('add/', add_snippet, name="add"),

    path('profile', profile, name="profile"),

    path('get-snippet-data/', get_snippets_data, name="get-snippet-data"),
]