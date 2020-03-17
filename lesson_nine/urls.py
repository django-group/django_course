from django.urls import path
from django_filters.views import FilterView

from lesson_nine import models
from lesson_nine import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list_url'),
    path('product/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail_url'),
    path('comment/<slug:slug>/', views.ReviewList.as_view(), name='review_list_url'),
    path('search/', views.SearchView.as_view(), name='search_url'),
    # path('filter/', FilterView.as_view(model=models.Product))
    path('create_product/', views.CreateProductView.as_view(), name='create_product_url'),
]
