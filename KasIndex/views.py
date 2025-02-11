from django.shortcuts import render, get_object_or_404
from .models import Actor, Serie, Pelicula, Television, Foto, Curriculum, Demo, Social, Client, Icon

def index_view(request):
    actores_especiales = Actor.objects.filter(especial=True)  # Obtén solo los actores especiales
    actores_normales = Actor.objects.filter(especial=False)   # Obtén los actores normales
    clientes = Client.objects.all()  # Asumiendo que tienes un modelo de Cliente para los clientes
    
    # Pasar todo al contexto
    context = {
        'actores_especiales': actores_especiales,
        'actores_normales': actores_normales,
        'clientes': clientes
    }
    
    return render(request, 'KasIndex/index.html', context)

def actor_detail(request, nombre):
    actor = get_object_or_404(Actor, nombre=nombre)
    series = Serie.objects.filter(actor=actor)
    peliculas = Pelicula.objects.filter(actor=actor)
    televisiones = Television.objects.filter(actor=actor)
    fotos = Foto.objects.filter(actor=actor)
    curriculum = Curriculum.objects.filter(actor=actor).first()
    demo = Demo.objects.filter(actor=actor).first()
    social = getattr(actor, 'social', None)
    icons = Icon.objects.filter(social=social)

    context = {
        'actor': actor,
        'series': series,
        'peliculas': peliculas,
        'televisiones': televisiones,
        'fotos': fotos,
        'curriculum': curriculum,
        'demo': demo,
        'social': social,
        'icons': icons,
    }

    return render(request, 'Kasindex/actor.html', context)


def contact_view(request):
    return render(request, 'KasIndex/contact_us.html')