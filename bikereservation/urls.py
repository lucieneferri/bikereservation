from django.contrib import admin
from django.urls import path, include
from reservation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pagina1/', views.pagina1, name='pagina1'),
    path('pagina2/', views.pagina2, name='pagina2'),
    path('accounts/', include('django.contrib.auth.urls')),
]
