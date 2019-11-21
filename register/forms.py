from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label=(""),
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password2 = forms.CharField(
        label=(""),
        widget=forms.PasswordInput(attrs={"placeholder": "Password confirmation"}),
        strip=False
    )
    first_name = forms.CharField(label="", max_length=30, required=True,
                                 widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    last_name = forms.CharField(label="", max_length=30, required=True,
                                widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    email = forms.EmailField(label="", max_length=70, required=True,
                             widget=forms.TextInput(attrs={"placeholder": "Email"}))
    username = forms.CharField(label="", max_length=100, required=True,
                               widget=forms.TextInput(attrs={"placeholder": "Username"}))
    ads = forms.BooleanField(label="", initial=True)

    class Meta:
        model = User
        fields = ('username', "first_name", "last_name", "email", "password1", "password2", "ads", )
