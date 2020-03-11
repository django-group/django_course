from django.contrib import admin


from lesson_nine import models

admin.site.register(models.Product)

admin.site.register(models.Review)

admin.site.register(models.Categories)
