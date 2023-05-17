from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reservation.models import SpinningBike, Reservation
from django.http.request import HttpRequest
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import get_user


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
def create_reservation(requests: HttpRequest):
    user = get_user(requests)
    date = requests.POST["date"]
    bike_id = int(requests.POST["bike_id"])
    bike = SpinningBike.objects.get(id=bike_id)

    if date:
        date_time = datetime.strptime(date, "%Y-%m-%dT%H:%M")
        date_timezone = timezone.make_aware(date_time)
        Reservation.objects.create(reservation_date=date_timezone, bike=bike, user=user)
    else:
        raise ValidationError({"date": "Você precisa selecionar uma data"})

    return redirect("list_reservations")

@login_required
def list_reservations(requests):
    user_id = requests.user.id
    reservations = Reservation.objects.filter(user_id=user_id)

    context = {'reservations':reservations}
    return render(requests, 'reservation.html', context)