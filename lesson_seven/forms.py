from django.forms import ModelForm
from lesson_seven.models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text']