from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from lesson_nine import models

admin.site.register(models.Product)

admin.site.register(models.Review)

admin.site.register(models.Categories)


class ProfileInLine(admin.StackedInline):
    model = models.UserProfile
    can_delete = False
    verbose_name_plural = 'User profile'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInLine, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)