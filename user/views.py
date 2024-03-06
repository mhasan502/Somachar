from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from user.forms import RegistrationForm, LoginForm, PasswordResetForm


class LoginView(View):
    """
    Login View
    """
    def get(self, request):
        """
        Get Request
        """
        if request.user.is_authenticated:
            return redirect('Index')
        else:
            login_form = LoginForm()
            return render(request, 'login.html', {'login_form': login_form})

    def post(self, request):
        """
        Post Request
        """
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are now logged in as {username}.')
                return redirect('Index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
        return render(request, 'login.html', {'login_form': login_form})


# Register Functionality
def register_view(request):
    register_view_form = None

    if request.method == 'GET' and request.user.is_authenticated is False:
        register_view_form = RegistrationForm()

    if request.method == 'POST':
        register_view_form = RegistrationForm(request.POST)
        if register_view_form.is_valid():
            user = register_view_form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Registration successful.')
            return redirect('Index')
        messages.error(request, 'Unsuccessful registration. Invalid information.')

    return render(request, 'signup.html', {'register_form': register_view_form})


class LogoutView(View):
    """
    Logout View
    """
    @login_required
    def dispatch(self, request, *args, **kwargs):
        """
        looks at the request and decides whether the GET or POST method of the view class should handle the request
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        """
        Get Request
        """
        logout(request)
        return redirect('Index')


# Password Reset Functionality
def password_reset_request(request):
    password_reset_form = None

    if request.method == 'GET':
        password_reset_form = PasswordResetForm()

    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = 'Password Reset Requested'
                    email_template_name = 'registration/password_reset_email.txt'
                    email_info = {
                        'email': user.email,
                        'domain': request.META['HTTP_HOST'],
                        'site_name': 'Somachar',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, email_info)
                    try:
                        send_mail(subject, email, 'admin@somachar.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect('/password_reset/done/')

    return render(request, 'registration/password_reset.html', {'password_reset_form': password_reset_form})
