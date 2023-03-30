from django.shortcuts import render
from .models import *

# Create your views here.


LANDING_HTML = 'landing/landing.html'


def barbers(request):
    context = {}

    barbers_foto = BarberFoto.objects.filter(is_active=True)

    context['barbers_foto'] = barbers_foto

    return render(request, LANDING_HTML, context=context)