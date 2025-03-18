from django.shortcuts import render, get_object_or_404, redirect
from .models import Actor, Serie, Pelicula, Television, Foto, Curriculum, Demo, Social, Client
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


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

    context = {
        'actor': actor,
        'series': series,
        'peliculas': peliculas,
        'televisiones': televisiones,
        'fotos': fotos,
        'curriculum': curriculum,
        'demo': demo,
        'social': social,
    }

    return render(request, 'Kasindex/actor.html', context)



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        actor = request.POST.get('actor')

        # Email content
        subject = f'New Contact Request for {actor}'
        message = f'''
        Contact Details:
        Name: {name}
        Phone: {phone}
        Email: {email}
        Interested in Actor: {actor}
        '''
        
        try:
            # Send email
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],  # Send to yourself or specific email
                fail_silently=False,
            )
            messages.success(request, '¡Mensaje enviado exitosamente!')
            return redirect('contact')
        except Exception as e:
            messages.error(request, 'Hubo un error al enviar el mensaje. Por favor, intente nuevamente.')
            return redirect('contact')

    return render(request, 'KasIndex/contact_us.html')