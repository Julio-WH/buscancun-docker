from django.contrib import admin

from apps.chofer.models import Chofer


# Register your models here.

@admin.register(Chofer)
class Chofer(admin.ModelAdmin):
    model = Chofer