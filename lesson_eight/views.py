from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import generic
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


from lesson_eight import forms, models


class MainView(generic.TemplateView):
    template_name = 'lesson_eight/ajax.html'
    human_form = forms.HumanForm

    def get(self, request, *args, **kwargs):
        ctx = {}
        ctx['script'] = 'alert(5555555);'
        if request.user.is_authenticated:
            all_humans = models.Human.objects.all()
            ctx['humans'] = all_humans
            ctx['human_form'] = self.human_form
            return render(request, self.template_name,  ctx)
        else:
            return render(request, self.template_name, ctx)


class RegisterFormView(generic.FormView):
    form_class = forms.Asd
    success_url = "/accounts/login"
    template_name = "lesson_eight/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


def validate_email(request):
    if request.GET:
        email = request.GET.get('email')
        is_taken = User.objects.filter(email=email).exists()
        if is_taken:
            data = {
                "is_taken" : "На этот почтовый ящик уже зарегистрирован пользователь!"
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'ok': "На этот почтовый адрес не было регистраций"})


def show_three(request):
    first_three = models.Human.objects.all()[:3].values()
    context = {
        'elements': list(first_three)
    }
    return JsonResponse(context)


def show_four(request):

    last_four = models.Human.objects.all()[:4].values()
    context = {
        'elements': list(last_four)
    }
    return JsonResponse(context)


@csrf_exempt
def add_human(request):
    if request.POST:
        if request.is_ajax():
            name = request.POST['name']
            surname = request.POST['surname']
            birth = request.POST['birth']
            company = request.POST['company']
            position = request.POST['position']
            language = request.POST['language']
            salary = request.POST['salary']
            human = models.Human.objects.create(name=name,
                                                surname=surname,
                                                birth=birth,
                                                company=company,
                                                position=position,
                                                language=language,
                                                salary=salary
                                                )
            return JsonResponse(human.dict())

