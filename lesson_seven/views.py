from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from lesson_seven import forms


def test_view(request):
    form_comment = forms.CommentForm(request.POST)
    if request.method == "POST":
        form_comment.save()
    context = {
        "form_comment": form_comment
    }
    return render(request, 'lesson_seven/test.html', context)


def auth_test(request):
    return render(request, 'lesson_seven/if_auth.html')


@login_required
def login_test(request):
    return HttpResponse('You are loggined')
