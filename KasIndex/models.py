from django.db import models

# Create your models here.
class Actor(models.Model):
    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="actor/")
    biografia = models.TextField()
    especial = models.BooleanField(default=False)


class Serie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='series')
    nombre = models.CharField(max_length=100)
    portada = models.ImageField(upload_to="actor/series/")
    plataforma=models.CharField(max_length=50, default="")

class Pelicula(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='peliculas')
    nombre = models.CharField(max_length=100)
    portada = models.ImageField(upload_to="actor/peliculas/")
    plataforma=models.CharField(max_length=50, default="")
class Television(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='television')
    nombre = models.CharField(max_length=100)
    portada = models.ImageField(upload_to="actor/television/")
    televisora = models.CharField(max_length=50, default="")

class Foto(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to="actor/imagenes/")

class Curriculum(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='curriculum')
    archivo = models.FileField(upload_to="actor/curriculum/")

class Demo(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='demo')
    video = models.FileField(upload_to="actor/video/", null=False)

class Social(models.Model):
    actor = models.OneToOneField(Actor, on_delete=models.CASCADE, related_name='social')
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)

class Client(models.Model):
    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="clientes/")