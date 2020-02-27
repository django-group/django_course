from django.shortcuts import render, HttpResponse
from django.views import generic

from lesson_five import forms


def search_form(request):
    return render(request, 'lesson_five/search_form.html')


def search(request):
    if request.method == "GET":
        if 'q' in request.GET:
            return HttpResponse("Вы хотели найти %s" % request.GET['q'])
        else:
            return HttpResponse("Вы отправили пустую форму")


def file_input(request):
    name = request.POST['name']
    surname = request.POST['surname']
    birth = request.POST['birth']
    gender = request.POST['gender']

    with open("some.txt", "w") as file:
        file = open("some.txt", "w")
        file.write("Имя :" + name + "\n")
        file.write("Фамилия :" + surname + "\n")
        file.write("Дата рождения :" + birth + "\n")
        file.write("Пол :" + gender + "\n")

    return HttpResponse("Данные успешно были записаны!")


def form(request):
    form_for_author1 = forms.AuthorOneForm
    form_for_article = forms.ArticleForm
    context = {
        'form_for_author1': form_for_author1,
        'form_for_article': form_for_article,
    }
    return render(request, 'lesson_five/form.html', context)


def author_add(request):
    form = forms.AuthorOneForm(request.POST)

    if request.method == "POST":

        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print(data)
            return HttpResponse("Автор добавлен!")


def add_article(request):
    form = forms.ArticleForm(request.POST)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        print(data)
        form.save()
        return HttpResponse("Статья добавлена!")


def contact_form(request):
    form = forms.ContactForm
    return render(request, 'lesson_five/contact_form.html', {'form': form})


class ContactFormView(generic.TemplateView):

    form_contact = forms.ContactForm

    def post(self, request):
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            return HttpResponse('Done!')

        return render(request, 'lesson_five/contact_form.html', {'form': form})

    def get(self, request):
        return render(request, 'lesson_five/contact_form.html', {'form': self.form_contact})


class UrlView(generic.TemplateView):
    form_submit_url = forms.UrlForm

    def post(self, request):
        form = forms.UrlForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
        else:
            print('invalid')
            context = {
                'form_url': form
            }
            return render(request, 'lesson_five/url_form.html', context)
        return HttpResponse(form.cleaned_data.items())

    def get(self, request):
        context = {
            'form_url': self.form_submit_url
        }
        return render(request, 'lesson_five/url_form.html', context)


