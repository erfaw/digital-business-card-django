from django import forms

class LoginForm(forms.Form): # TODO (MID) refactor this with AuthenticationForm
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
        )
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


class RegisterForm(forms.Form): # TODO (MID) refactor this form with built-in for register forms in django. 
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
