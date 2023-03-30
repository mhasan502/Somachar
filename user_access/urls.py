from django.urls import re_path
from django.urls import path
from django.contrib.auth import views as auth_views
from .api import UserList
from .views import register_view, login_view, logout_view, password_reset_request


urlpatterns = [
    # Register Page
    path('signup/', register_view, name='Signup'),
    # Login Page
    path('login/', login_view, name='Login'),
    # Logout Page
    path('logout/', logout_view, name='Logout'),

    # User API
    re_path(r'user/(?P<uname>[._A-Za-z0-9]+)/$', UserList.as_view()),

    # Password Reset Pages
    re_path(r'^password_reset/$', password_reset_request, name='Password Reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]
