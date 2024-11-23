from django import forms
from apps.accaunts.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError




class UserForm(forms.ModelForm):
    uzb_phone_regex = RegexValidator(
        regex=r'^\+998\d{9}$',
        message=("Phone number must be entered in the format: '+998XXXXXXXXX'.")
    )
    phone = forms.CharField(validators=[uzb_phone_regex], max_length=13, label="Enter your phone")

    email = forms.EmailField(label="Enter your email: ")

    password1 = forms.CharField(
        label = ("Password"),
        strip = False,
        widget=forms.PasswordInput(attrs={"autocomplate": "new-password"}),
    )
    password2 = forms.CharField(
        label = ("Password confirmation"),
        strip = False,
        widget=forms.PasswordInput(attrs={"autocomplate": "new-password"}),
    )

    def clean(self):
        data = super().clean()
        pass1 = data.get('password1')
        pass2 = data.get('password2')
        if pass1:
            try:
                validate_password(pass1)
            except ValidationError as e:
                self.add_error('password1', e)
        if pass1 != pass2:
            raise forms.ValidationError("Parollar Mos Emas!")
        return data

    class Meta:
        model = User
        fields = ['phone', 'email', 'password1', 'password2',]