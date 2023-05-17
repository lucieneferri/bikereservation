from django.db import models
from django.contrib.auth.models import User


class SpinningBike(models.Model):
    bike_number = models.CharField(max_length=10)

    def __str__(self):
        return self.bike_number


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(SpinningBike, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.user.username} reservou a bicicleta número {self.bike.bike_number} na data {self.reservation_date}"