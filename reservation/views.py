from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reservation.models import SpinningBike, Reservation
from django.http.request import HttpRequest
from django.core.exceptions import ValidationError


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
    # import ipdb;ipdb.set_trace()
    date = requests.GET.get('date')
    available_bikes = SpinningBike.objects.exclude(
        id__in=Reservation.objects.filter(reservation_date=date).values('bike_id')
    )
    context = {'available_bikes': available_bikes, 'date': date}
    return render(requests, 'home.html', context)

@login_required
def create_reservation(requests: HttpRequest):
    # import ipdb;ipdb.set_trace()
    user_id = requests.user.id
    date = requests.POST["date"]
    bike_id = requests.POST["bike_id"]

    # print("User ID:", user_id)
    # print("Date:", date)
    # print("Bike ID:", bike_id)

    if date:
        bike_id = requests.POST.get("bike_id")
        Reservation.objects.create(reservation_date=date, bike_id=bike_id, user_id=user_id)
    else:
        raise ValidationError({"date": "Você precisa selecionar uma data"})

    return redirect("list_reservations")

@login_required
def list_reservations(requests):
    user_id = requests.user.id
    reservations = Reservation.objects.filter(user_id=user_id)

    context = {'reservations':reservations}
    return render(requests, 'reservation.html', context)