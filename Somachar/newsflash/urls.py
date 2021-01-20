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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from speech import views as SpeechView


urlpatterns = [
    # Home Page
    path('', TemplateView.as_view(template_name="index.html"), name="Index"),
    # Admin Access Page
    path('admin/', admin.site.urls),
    # User functionality
    path('', include('user_access.urls')),
    # News Page
    path("news/", SpeechView.newsView, name='news'),
    # Api Urls
    path('api/', include('news.urls'), name='News'),
    # Token Generate
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Others
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
