from rest_framework import serializers

from reservation.models import SpinningBike, Reservation

class SpinningBikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpinningBike
        fields = ["bike_number"]


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["user", "bike", "reservation_date"]