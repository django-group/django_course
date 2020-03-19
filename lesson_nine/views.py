from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, Http404
from django.urls import reverse
import json
import random

from lesson_nine import models
from lesson_nine import forms
from lesson_nine import filters


class ProductDetail(generic.DetailView):
    models = models.Product
    template_name = 'lesson_nine/produt_detail.html'
    context_object_name = 'product'
    comment_form = forms.CommentCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = self.comment_form
        return context

    def get_queryset(self):
        product = models.Product.objects.filter(slug=self.kwargs.get("slug"))
        return product

    def post(self, request, *args, **kwargs):
        form = self.comment_form(request.POST)
        if form.is_valid():
            obj = self.get_object()
            form.instance.product = obj
            form.save()
            return redirect(reverse('review_list_url', args=[obj.slug]))


class ReviewList(generic.ListView):
    model = models.Review
    template_name = 'lesson_nine/review_list.html'
    paginate_by = 3

    def get_queryset(self):
        product = get_object_or_404(models.Product, slug=self.kwargs.get('slug'))
        review = models.Review.objects.filter(product=product)
        return review


class SearchView(generic.ListView):
    form = forms.SearchForm
    model = models.Product
    template_name = 'lesson_nine/products_list.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        search_value = self.request.GET.get('search_field')
        search_value = models.Product.objects.filter(name__contains=search_value)
        if not search_value:
            raise Http404
        context['object_list'] = search_value
        return context


class ProductList(generic.ListView):
    form = forms.SearchForm
    filter = filters.ProductFilter
    model = models.Product
    template_name = 'lesson_nine/products_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        object_list = self.filter(self.request.GET, queryset=self.model.objects.all())

        context['object_list'] = object_list.qs
        context['form'] = self.form
        context['filter'] = self.filter

        return context

#
# class ProductList(generic.ListView):
#     form = forms.SearchForm
#     model = models.Product
#     template_name = 'lesson_nine/products_list.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = self.form
#         if 'search' in self.request.path:
#             context['object_list'] = models.Product.objects.filter(name__icontains=self.request.GET.get('search_field'))
#         return context


class CreateProductView(generic.CreateView):
    model = models.Product
    template_name = 'lesson_nine/create_product.html'
    form_class = forms.ProductCreateForm

    def form_valid(self, form):
        form.save()
        return redirect(reverse('product_detail_url', args=[form.instance.slug]))


def add_to_bucket(request, slug):
    bucket_key = request.COOKIES.get('bucket', '')
    if not bucket_key:
        bucket_key = str(random.randint(1, 10000))

    product = models.Product.objects.get(slug=slug)
    # try:
    #     bucket = models.Bucket.objects.get(session_key=bucket_key)
    # except:
    #     bucket = models.Bucket.objects.create(session_key=bucket_key)

    bucket, _ = models.Bucket.objects.get_or_create(session_key=bucket_key)
    bucket.save()
    bucket.product.add(product)
    response = redirect(reverse('product_detail_url', args=[slug]))
    response.set_cookie('bucket', bucket_key)
    return response


def bucket_view(request):
    bucket_key = request.COOKIES.get('bucket', '')
    bucket = models.Bucket.objects.filter(session_key=bucket_key)
    if bucket:
        products = bucket[0].product.all()
    else:
        products = None
    context = {
        'product': products
    }
    return render(request, 'lesson_nine/bucket.html', context)


# def add_to_bucket(request, slug):
#     session_key = request.session.get('bucket', [])
#     if not session_key:
#         session_key = str(random.randint(1, 10000))
#         request.session['bucket'] = session_key
#
#     product = models.Product.objects.get(slug=slug)
#     bucket, created = models.Bucket.objects.get_or_create(session_key=session_key)
#     bucket.save()
#     bucket.product.add(product)
#     response = redirect(reverse('product_detail_url', args=[slug]))
#     return response
#
#
# def bucket_view(request):
#     session_key = request.session.get('bucket', '')
#     bucket = models.Bucket.objects.filter(session_key=session_key)
#     if bucket:
#         products = bucket[0].product.all()
#     else:
#         products = None
#     context = {
#         'bucket': products
#     }
#     return render(request, 'lesson_nine/bucket.html', context)
