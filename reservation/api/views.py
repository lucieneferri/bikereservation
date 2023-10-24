from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reservation.api.serializers import SpinningBikeSerializer
from reservation.models import SpinningBike, Reservation
from django.http.request import HttpRequest
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import get_user
from rest_framework.generics import ListAPIView

class BikeListView(ListAPIView):
    queryset = SpinningBike.objects.all()
    serializer_class = SpinningBikeSerializer

@login_required
def home(requests):
    return render(requests, 'home.html')

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

@login_required
def cancel_reservation(requests):
    reservation_id = requests.POST["reservation_id"]
    reservation = Reservation.objects.get(id=reservation_id)
    reservation.delete()

    return redirect("list_reservations")