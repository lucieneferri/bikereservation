from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reservation.models import SpinningBike, Reservation
from django.http.request import HttpRequest


@login_required
def home(requests):
    return render(requests, 'home.html')

@login_required
def pagina1(requests):
    return render(requests, 'pagina1.html')

@login_required
def pagina2(requests):
    return render(requests, 'pagina2.html')

@login_required
def available_bikes(requests):
    date = requests.GET.get('date')
    available_bikes = SpinningBike.objects.exclude(
        id__in=Reservation.objects.filter(reservation_date=date).values('bike_id')
    )
    context = {'available_bikes': available_bikes, 'date': date}
    return render(requests, 'home.html', context)

@login_required
def create_reservation(requests: HttpRequest, bike_id):
    date = requests.POST["date"]
    user_id = requests.user.id
    Reservation.objects.create(reservation_date=date, bike_id=bike_id, user_id=user_id)

    return redirect("reservations")

@login_required
def list_reservations(requests):
    user_id = requests.user.id
    reservations = Reservation.objects.filter(user_id=user_id)

    context = {'reservations':reservations}
    return render(requests, 'reservation.html', context)