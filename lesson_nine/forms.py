from django import forms

from lesson_nine import models


class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=100)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['rating', 'good', 'bad', 'text']


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'description', 'image', 'price', 'category']