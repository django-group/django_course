from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from lesson_eight import models


class HumanForm(forms.ModelForm):
    class Meta:
        model = models.Human
        fields = [field.name for field in models.Human._meta.fields]


class Asd(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(Asd, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
