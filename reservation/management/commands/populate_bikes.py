from django.core.management.base import BaseCommand
from reservation.models import SpinningBike

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        bikes = [
            {'bike_number': '1'},
            {'bike_number': '2'},
            {'bike_number': '3'},
            {'bike_number': '4'},
            {'bike_number': '5'},
            {'bike_number': '6'},
        ]

        for bike in bikes:
            SpinningBike.objects.create(**bike)
        self.stdout.write(self.style.SUCCESS('Banco populado com sucesso!'))