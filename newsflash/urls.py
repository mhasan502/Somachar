"""newsflash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

from user_access import views as userView
from django.contrib.auth import views as auth_views
from speech import views as SpeechView


urlpatterns = [
    # Home Page
    path('', TemplateView.as_view(template_name="index.html"), name="Index"),
    # Admin Access Page
    path('admin/', admin.site.urls),
    # Register Page
    path('signup/', userView.register_view, name='Signup'),
    # Login Page
    path('login/', userView.login_view, name='Login'),

    # Password Reset Pages
    url(r'^password_reset/$', userView.password_reset_request, name='Password Reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),

    # Speech Recognition Pages
    path("news/", SpeechView.newsView, name='news'),
    path('api/', include('news.urls'), name='News'),
    # API
    path('hello/', include('user_access.urls')),
    # Token Generate
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Others
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
