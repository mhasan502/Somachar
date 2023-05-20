from django.contrib import admin
from django.urls import include, path
from .views import IndexView

# Social Login Urls
social_auth_patterns = ([
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
])

# Admin Urls
admin_pattern = ([
    path('admin/', admin.site.urls),
])

urlpatterns = [
    path('', IndexView, name="Index"),

    # App Urls
    path(r'', include('news.urls'), name='News'),
    path(r'', include('user.urls')),

    # Other Patterns
    path(r'', include(social_auth_patterns)),
    path(r'', include(admin_pattern)),

]
