from django.contrib import admin
from .models import Restaurant, Meal, Reservation
admin.site.register(Restaurant)
admin.site.register(Meal)
admin.site.register(Reservation)
