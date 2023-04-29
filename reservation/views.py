from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reservation.models import SpinningBike, Reservation

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