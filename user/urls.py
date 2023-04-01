from django.contrib.auth import views as auth_views
from django.urls import re_path, include
from .api import UserList
from .views import register_view, login_view, logout_view, password_reset_request

# Password Reset URLs
password_reset_patterns = ([
    re_path(r'^password_reset/$', password_reset_request, name='Password Reset'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>\w+)/(?P<token>\w+)/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),
])

urlpatterns = [
    re_path('signup/', register_view, name='Signup'),
    re_path('login/', login_view, name='Login'),
    re_path('logout/', logout_view, name='Logout'),

    # User API
    re_path(r'user/(?P<username>[._A-Za-z0-9]+)/$', UserList.as_view()),

    re_path(r'^', include(password_reset_patterns)),
]
