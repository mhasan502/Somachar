from django.contrib import admin
from django.urls import include, re_path
from .views import IndexView

# URLS ########## //TODO
from .views import EditIndex
# URLS ##########

# Social Login Urls
social_auth_patterns = ([
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
])

# Admin Urls
admin_pattern = ([
    re_path(r'^admin/', admin.site.urls),
])


# UI Update Urls //TODO
ui_edit_pattern = ([
    re_path(r'^edit/', EditIndex),
])

urlpatterns = [
    re_path(r'^$', IndexView, name="Index"),

    # App Urls
    re_path(r'', include('news.urls'), name='News'),
    re_path(r'', include('user.urls')),

    # Other Patterns
    re_path(r'', include(social_auth_patterns)),
    re_path(r'', include(admin_pattern)),

    # UI Update Urls //TODO
    re_path(r'', include(ui_edit_pattern)),

]
