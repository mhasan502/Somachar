from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

default_class = 'input100 bg-gray-200 border rounded-md text-x font-medium leading-6 text-gray-800 py-3 w-full pl-3 mt-2'


# Register form
class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': default_class,
                'placeholder': 'Type your Username',
            }
        ),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': default_class,
                'placeholder': 'Type your First Name',
            }
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': default_class,
                'placeholder': 'Type your Last Name',
            }
        ),
    )
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': default_class,
                'placeholder': 'Type your Email',
            }
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': default_class,
                'placeholder': 'Type your Password',
                'id': 'pass',
            }
        ),
    )
    retype_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': default_class,
                'placeholder': 'Retype your Password',
            }
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'retype_password',)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# Login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': default_class,
                'id': 'username',
                'placeholder': 'Type your Username',
            }
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': default_class,
                'id': 'pass',
                'placeholder': 'Type your Password',
            }
        ),
    )
