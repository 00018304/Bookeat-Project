from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Meal, Reservation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django import forms
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['restaurant', 'datetime', 'guests', 'meals', 'note']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'meals': forms.CheckboxSelectMultiple,
        }
def home(request):
    restaurants = Restaurant.objects.all()[:3]
    return render(request, 'bookeat/home.html', {'restaurants': restaurants})
def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    meals = restaurant.meals.all()[:10]
    return render(request, 'bookeat/restaurant_detail.html', {'restaurant': restaurant, 'meals': meals})
@login_required
def reservations_list(request):
    res = Reservation.objects.filter(user=request.user)
    return render(request, 'bookeat/reservations_list.html', {'reservations': res})
@login_required
def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            r = form.save(commit=False)
            r.user = request.user
            r.save()
            form.save_m2m()
            return redirect('bookeat:reservations_list')
    else:
        form = ReservationForm()
    return render(request, 'bookeat/reservation_form.html', {'form': form, 'create': True})
@login_required
def reservation_edit(request, pk):
    r = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=r)
        if form.is_valid():
            form.save()
            return redirect('bookeat:reservations_list')
    else:
        form = ReservationForm(instance=r)
    return render(request, 'bookeat/reservation_form.html', {'form': form, 'create': False})
@login_required
def reservation_delete(request, pk):
    r = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        r.delete()
        return redirect('bookeat:reservations_list')
    return render(request, 'bookeat/reservation_confirm_delete.html', {'reservation': r})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'bookeat/register.html', {'form': form})

