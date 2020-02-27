from django.contrib import admin
from . import models


admin.site.register(models.Example)

admin.site.register(models.Book)
admin.site.register(models.Place)
admin.site.register(models.Restaurant)
admin.site.register(models.Publication)
admin.site.register(models.Article)
# admin.site.register(models.Author)


class AuthorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Author._meta.fields]
    fields = ['name', 'surname']
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = models.Author


admin.site.register(models.Author, AuthorAdmin)