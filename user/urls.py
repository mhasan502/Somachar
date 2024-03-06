from django.contrib.auth import views as auth_views
from django.urls import path, include
from .api import UserList
from .views import register_view, LoginView, LogoutView, password_reset_request

# Password Reset URLs
password_reset_patterns = ([
    path('password_reset/', password_reset_request, name='Password Reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
])

urlpatterns = [
    path('signup/', register_view, name='Signup'),
    path('login/', LoginView.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),

    # User API
    path('user/<username>/', UserList.as_view()),

    path('', include(password_reset_patterns)),
]
