from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(requests):
    return render(requests, 'home.html')

@login_required
def pagina1(requests):
    return render(requests, 'pagina1.html')

@login_required
def pagina2(requests):
    return render(requests, 'pagina2.html')




