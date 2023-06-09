from django.contrib import admin
from django.urls import path, include
from reservation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('available_bikes/', views.available_bikes, name='available_bikes'),
    path('reservation/', views.create_reservation, name='create_reservation'),
    path('reservations/', views.list_reservations, name='list_reservations'),
    path('cancel_reservation/', views.cancel_reservation, name='cancel_reservation')
]
