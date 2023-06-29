from django.contrib import admin

from apps.chofer.models import Chofer, Autobus


# Register your models here.

@admin.register(Chofer)
class Chofer(admin.ModelAdmin):
    model = Chofer


@admin.register(Autobus)
class Autobus(admin.ModelAdmin):
    model = Autobus