from django.contrib import admin

from .models import CustomUser
admin.site.register(CustomUser)
# Register your models here.

from .models import Notes
admin.site.register(Notes)
