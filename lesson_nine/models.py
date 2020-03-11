from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

# CATEGORIES = [
#     ('pc', 'Ноутбуки и компьютеры'),
#     ('phones_tv_electronics', 'Смартфоны, ТВ и електроника'),
#     ('appliances', 'Бытовая техника'),
#     ('home_tech', 'Товары для тома'),
#     ('instruments_and_auto', 'Инструменты и автотовары'),
#     ('plumbing', 'Сантехника'),
#     ('garden', 'Дача, сад, огород'),
#     ('wear', 'Одежда'),
#     ('child', 'Товары для детей')
# ]


class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    price = models.FloatField()
    rating = models.FloatField(default=0)
    slug = models.SlugField(blank=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    in_stock = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name + ' | ' + self.category.category_name

    def get_comments(self):
        return Review.objects.filter(product=self)

    def count_comments(self):
        return len(Review.objects.filter(product=self))


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    good = models.TextField(default='...')
    bad = models.TextField(default='...')
    text = models.TextField()
