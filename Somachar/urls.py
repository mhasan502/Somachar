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
