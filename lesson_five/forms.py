from django.forms import ModelForm
from django import forms
from django.core.validators import URLValidator, ValidationError

from lesson_five import models

#
# class AuthorForm(forms.Form):
#     CHOICES_FOR_CITY = (
#         ('kyiv', "Киев"),
#         ('chernigov', "Чернигов"),
#         ('odessa', "Одесса"),
#         ('lvov', "Львов"),
#     )
#
#     name = forms.CharField(max_length=200)
#     surname = forms.CharField(max_length=200)
#     city = forms.ChoiceField(choices=CHOICES_FOR_CITY, required=False)
#
#     def save(self):
#         model = models.Author1(name=self.cleaned_data['name'],
#                                surname=self.cleaned_data['surname'],
#                                city=self.cleaned_data['city'])


class AuthorOneForm(ModelForm):
    class Meta:
        model = models.Author1
        fields = ['name', 'surname', 'city']


class ArticleForm(ModelForm):
    class Meta:
        model = models.Article
        fields = ['author', 'title', 'text']


class ContactForm(forms.Form):
    boolean_field = forms.NullBooleanField()    # NullBooleanField
    name_sender = forms.CharField(max_length=100, label="Введите ваше имя")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")
    sender = forms.EmailField(label="Введите ваш емейл!")


def validate_url(value):
    validation_url = URLValidator()
    value_one_invalid = False
    value_two_invalid = False
    try:
        validation_url(value)
    except:
        value_one_invalid = True

    value_two_url = 'http://' + value
    try:
        validation_url(value_two_url)
    except:
        value_two_invalid = True
    if value_one_invalid and value_two_invalid:
        raise forms.ValidationError("Неправильный адрес сайта!")
    return value


class UrlForm(forms.Form):
    title = forms.CharField(label='Название сайта')
    url = forms.CharField(label='Адрес сайта', validators=[validate_url])

    # def clean_title(self):
    #     return self.cleaned_data['title']

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     validation_url = URLValidator()
    #     try:
    #         validation_url(url)
    #     except:
    #         raise forms.ValidationError('Это не адрес сайта!')
    #     return url


