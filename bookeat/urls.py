from django.urls import path
from . import views
app_name = 'bookeat'
urlpatterns = [
    path('restaurants/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('reservations/', views.reservations_list, name='reservations_list'),
    path('reservations/create/', views.reservation_create, name='reservation_create'),
    path('reservations/<int:pk>/edit/', views.reservation_edit, name='reservation_edit'),
    path('reservations/<int:pk>/delete/', views.reservation_delete, name='reservation_delete'),
    path('register/', views.register, name='register'),
]
