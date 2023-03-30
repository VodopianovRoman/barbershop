from django.contrib import admin
from .models import *

# Register your models here.


class BarberFotoImageInline(admin.TabularInline):
    model = BarberFoto
    extra = 0


@admin.register(Barbers)
class BarbersAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [field.name for field in Barbers._meta.fields]
    list_display_links = ('id', 'barber_surname')
    list_filter = ('id', 'barber_surname', 'barber_category')
    search_fields = ('id', 'barber_surname', 'barber_category')
    inlines = [BarberFotoImageInline, ]


@admin.register(BarberFoto)
class BarberFotoAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [field.name for field in BarberFoto._meta.fields]
    list_display_links = ('id', 'barber')
    list_filter = ('id', 'barber')


@admin.register(Category)
class StatusOrder(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [field.name for field in Category._meta.fields]
    list_display_links = ('id', 'category')
    list_filter = ('category',)