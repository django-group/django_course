from django.urls import path

from lesson_seven import views

urlpatterns = [
    path('', views.auth_test),
    path('login_test/', views.login_test),
]