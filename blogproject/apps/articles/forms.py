from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegiserForm(UserCreationForm):
    username = forms.CharField(label="Username", help_text="Maximum length of username is 150 characters",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last Name",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", help_text="Minimum length of password is 8 letters",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", help_text="Confirm the password you provide higher",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
