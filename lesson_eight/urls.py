from django.urls import path

from lesson_eight import views

urlpatterns = [
    path('', views.MainView.as_view()),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('validate-email/', views.validate_email, name='validate_email'),
    path('show-three/', views.show_three, name='show_three'),
    path('show-four/', views.show_four, name='show_four'),
    path('add-human/', views.add_human, name='add_human'),
]
