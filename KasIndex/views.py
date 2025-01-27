from django.shortcuts import render
from .models import Actor

def index_view(request):
    actores_especiales = Actor.objects.filter(especial=True)  # Obtén solo los actores especiales
    return render(request, 'KasIndex/index.html', {'actores_especiales': actores_especiales})

def actor_view(request):
    return render(request, 'KasIndex/actor.html')

def contact_view(request):
    return render(request, 'KasIndex/contact_us.html')