from django.db import models
from django.contrib.auth.models import User
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    def __str__(self): return self.name
class Meal(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='meals')
    name = models.CharField(max_length=200)
    is_drink = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    def __str__(self): return self.name
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    guests = models.PositiveIntegerField(default=1)
    meals = models.ManyToManyField(Meal, blank=True)
    note = models.TextField(blank=True)
    def __str__(self): return f"Reservation {self.pk} by {self.user} at {self.restaurant}"
