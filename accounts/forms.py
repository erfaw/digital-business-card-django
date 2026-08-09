from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class LoginForm(forms.Form):  # TODO (MID) refactor this with AuthenticationForm
    username = forms.CharField(
        min_length=4,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "cf-input",
                "type": "text",
                "id": "cfName",
                "name": "username",
                "data-i18n-ph": "cf_name_ph",
                "autocomplete": "username",
                "required": True,
            }
        ),
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                "class": "cf-input",
                "type": "password",
                "id": "cfName",
                "name": "password",
                "data-i18n-ph": "cf_name_ph",
                "autocomplete": "current-password",
                "required": True,
            }
        ),
    )


class RegisterForm(forms.Form):  # TODO (MID) refactor this form with built-in for register forms in django.
    full_name = forms.CharField(
        min_length=3,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "cf-input",
                "type": "text",
                "id": "cfName",
                "name": "full_name",
                "data-i18n-ph": "cf_name_ph",
                "autocomplete": "name",
                "required": True,
            }
        ),
    )
    username = forms.CharField(
        min_length=4,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "cf-input",
                "type": "text",
                "id": "cfName",
                "name": "username",
                "data-i18n-ph": "cf_name_ph",
                "autocomplete": "username",
                "required": True,
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "cf-input",
                "type": "email",
                "id": "cfName",
                "name": "email",
                "data-i18n-ph": "cf_name_ph",
                "autocomplete": "email",
                "required": True,
            }
        ),
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                "class": "cf-input",
                "type": "password",
                "id": "cfName",
                "name": "password",
                "data-i18n-ph": "cf_name_ph",
                "autocomplete": "new-password",
                "required": True,
            }
        ),
    )
    password2 = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                "class": "cf-input",
                "type": "password",
                "id": "cfName",
                "name": "password2",
                "data-i18n-ph": "cf_name_ph",
                "autocomplete": "new-password",
                "required": True,
            }
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get("password") == cleaned_data.get("password2"):
            raise forms.ValidationError(_("Passwords doesn't match!"))
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username__iexact=username).exists() or username.lower() == 'admin':
            raise forms.ValidationError(_("This username was taken already!"))
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("This email was taken already!"))
        return email
    