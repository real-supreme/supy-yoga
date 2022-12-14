from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import password_validation
from .models import UserModel, ProfileModel
from django import forms


class UsersForm(UserCreationForm):
    fullname = forms.CharField(
        max_length=100,
        required=True,
        strip=True,
        widget=forms.TextInput(attrs={"placeholder": "Full Name"}),
    )
    age = forms.IntegerField(
        required=True,
        min_value=18,
        max_value=85,
        widget=forms.TextInput(attrs={"placeholder": "Age (18-85)"}),
    )
    username = forms.CharField(
        max_length=100,
        required=True,
        strip=True,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Email"}),
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "placeholder": "Password"}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "placeholder": "Repeat Password"}
        ),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = UserModel
        fields = ("fullname", "age", "username", "email", "password1", "password2")


class AuthForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        strip=True,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "placeholder": "Password"}
        ),
    )

    class Meta:
        model = UserModel
        fields = ("username", "password")


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserModel
        fields = ["username", "email"]
