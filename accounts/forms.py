from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import STATE_CHOICES, GENDER_CHOICES


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    notes = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}), required=False)

    first_name = forms.CharField(required=True)
    surname = forms.CharField(required=True)

    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}))

    address = forms.CharField(required=True)
    suburb = forms.CharField(required=True)
    postcode = forms.CharField(required=True)
    state = forms.ChoiceField(choices=STATE_CHOICES, required=True)

    phone_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "surname",
            "gender",
            "date_of_birth",
            "address",
            "suburb",
            "postcode",
            "state",
            "phone_number",
            "notes",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        if commit:
            user.save()
        return user
