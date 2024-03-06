from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

DESIGN_CLASS = 'input100 bg-gray-200 border rounded-md text-x font-medium leading-6 text-gray-800 py-3 w-full pl-3 mt-2'


class RegistrationForm(UserCreationForm):
    """
    Register form and its fields
    """
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': DESIGN_CLASS,
                'placeholder': 'Type your Username',
            }
        ),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': DESIGN_CLASS,
                'placeholder': 'Type your First Name',
            }
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': DESIGN_CLASS,
                'placeholder': 'Type your Last Name',
            }
        ),
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': DESIGN_CLASS,
                'placeholder': 'Type your Email',
            }
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': DESIGN_CLASS,
                'placeholder': 'Type your Password',
                'id': 'pass',
            }
        ),
    )
    retype_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': DESIGN_CLASS,
                'placeholder': 'Retype your Password',
            }
        ),
    )

    class Meta:
        """
        Meta class for Registration form
        """
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'retype_password',)

    def save(self, commit=True):
        """
        Save user and its fields
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data['email'].lower()
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    """
    Login form and its fields
    """
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': DESIGN_CLASS,
                'id': 'username',
                'placeholder': 'Type your Username',
            }
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': DESIGN_CLASS,
                'id': 'pass',
                'placeholder': 'Type your Password',
            }
        ),
    )


class PasswordResetForm(forms.Form):
    """
    Password reset form
    """
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': DESIGN_CLASS,
                'placeholder': 'Type your Email',
            }
        ),
    )


class PasswordResetConfirmForm(forms.Form):
    """
    Password reset confirm form
    """
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': DESIGN_CLASS,
                'id': 'id_new_password1',
                'placeholder': 'Type your Password',
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': DESIGN_CLASS,
                'id': 'id_new_password2',
                'placeholder': 'Retype your Password',
            }
        ),
    )
