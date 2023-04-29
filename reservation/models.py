from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    pass


class SpinningBike(models.Model):
    bike_number = models.CharField(max_length=10)

    def __str__(self) -> str:
        return super().__str__()


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(SpinningBike, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.user.user_name} reserved bike {self.bike.bike_number}"