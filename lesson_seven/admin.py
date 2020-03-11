from django.contrib import admin


from lesson_seven import models
# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Article)
admin.site.register(models.Comments)