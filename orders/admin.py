from django.contrib import admin

# Register your models here.

from .models import Dish, Pasta, Pizza, Salad #Topping,

# Register your models here.
admin.site.register(Dish)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Pizza)
#admin.site.register(Topping)

