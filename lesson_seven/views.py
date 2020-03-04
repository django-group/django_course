from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def test_view(request):
    username = request.POST['username']
    password = request.POST['password']

    user = User.objects.create_user(username=username, password=password)

    user.save()


def auth_test(request):
    return render(request, 'lesson_seven/if_auth.html')


@login_required
def login_test(request):
    return HttpResponse('You are loggined')
