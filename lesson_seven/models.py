from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)
    b_day = models.DateField(auto_now=False)


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=20000)
    create_d = models.DateField(auto_now=True)


class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)