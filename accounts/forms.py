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
