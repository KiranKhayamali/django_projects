from django.contrib import admin
from .models import coffee

class coffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

# Register your models here.
admin.site.register(coffee, coffeeAdmin)