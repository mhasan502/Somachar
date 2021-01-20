from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
import user_access.views as userView
from user_access.api import UserList

urlpatterns = [
    # User API
    url(r'user/(?P<uname>[._A-Za-z0-9]+)/$', UserList.as_view()),

    # Register Page
    path('signup/', userView.register_view, name='Signup'),
    # Login Page
    path('login/', userView.login_view, name='Login'),
    # Logout Page
    path('logout/', userView.logout_view, name='Logout'),

    # Password Reset Pages
    url(r'^password_reset/$', userView.password_reset_request, name='Password Reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]
