from django.contrib import admin
from django.urls import path, include
from reservation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pagina1/', views.pagina1, name='pagina1'),
    path('pagina2/', views.pagina2, name='pagina2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('available_bikes/', views.available_bikes, name='available_bikes'),
    path('reservation/', views.create_reservation, name='create_reservation'),
    path('reservations/', views.list_reservations, name='list_reservations')
]
