from django.shortcuts import render, Http404

from lesson_four import models

# Create your views here.
def asd(request):
    test = models.Author.objects.filter(name='name')
    if not test:
        raise Http404('Cannt find')
    return render(request, 'asd.html', context={'test': test})


"""
{% for item in test %}
    {{ item.name }}
    {{ item.surname }}
{% endfor %}
"""

def model_view(request):
    # взять все
    models.Author.objects.all()
    # взять ОДНУ запись(в этом случае поиск по id)
    models.Author.objects.get(id=1)
    # взять несколько (в этом случае поиск всех записей у которых name='name')
    models.Author.objects.filter(name='name')
