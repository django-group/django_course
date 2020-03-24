from django import forms
import django_filters
from django.contrib.auth.models import User

from lesson_nine import models


class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=100, help_text='Write some request')


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['rating', 'good', 'bad', 'text']


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'description', 'image', 'price', 'category']


class SignupForm(forms.ModelForm):
    class Meta:
        models = User