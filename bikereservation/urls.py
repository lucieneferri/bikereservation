from django.urls import path, include

urlpatterns = [
    path('', include('reservation.api.urls'))
]
