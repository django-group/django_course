from django.urls import path

from lesson_four import views

urlpatterns = [
    path('', views.model_view),
]
