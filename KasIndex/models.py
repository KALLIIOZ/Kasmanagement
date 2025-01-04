from django.db import models

# Create your models here.
class Actor(models.Model):
    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="actor/")
    biografia = models.TextField()
    especial = models.BooleanField(default=False)


class Series(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='series')
    nombre = models.CharField(max_length=100)
    portada = models.ImageField(upload_to="actor/series/")
    plataforma = models.ImageField(max_length=50)

class Peliculas(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='peliculas')
    nombre = models.CharField(max_length=100)
    portada = models.ImageField(upload_to="actor/peliculas/")
    plataforma = models.ImageField(max_length=50)

class Television(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='television')
    nombre = models.CharField(max_length=100)
    portada = models.ImageField(upload_to="actor/television/")
    televisora = models.ImageField(max_length=50)

class Fotos(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to="actor/imagenes/")

class Curriculum(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='curriculum')
    archivo = models.FileField(upload_to="actor/curriculum/")

class Demo(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='demo')
    video = models.FileField(upload_to="actor/video/")

class Social(models.Model):
    Actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='social')
    facebook = models.URLField(blank=True, null=False)
    instagram = models.URLField(blank=True, null=False)
    twitter = models.URLField(blank=True, null=False)
    tiktok = models.URLField(blank=True, null=False)
