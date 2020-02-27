from django.urls import path

from lesson_five import views

urlpatterns = [
    path('search_form/', views.search_form),
    path('search/', views.search),
    path('file_input/', views.file_input),

    path('', views.form),
    path('add_article/', views.add_article, name='add_article'),
    path('add_author/', views.author_add, name='add_author'),

    # path('contact_form/', views.contact_form, name='contact_form'),

    path('contact_form/', views.ContactFormView.as_view(), name='contact_form'),

    path('url_form/', views.UrlView.as_view(), name='url_form')
]
