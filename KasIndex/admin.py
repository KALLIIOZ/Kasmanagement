from django.contrib import admin
from .models import Actor, Series, Peliculas, Television, Fotos, Curriculum, Demo, Social

# Register your models here.

class SeriesInline(admin.ModelAdmin):
    model = Series
    extra = 1
    fields = ('nombre', 'portada', 'plataforma')

class PeliculasInline(admin.ModelAdmin):
    model = Peliculas
    extra = 1
    fields = ('nombre', 'portada', 'plataforma')

class TelevisionInline(admin.ModelAdmin):
    model = Television
    extra = 1
    fields = ('nombre', 'portada', 'plataforma')

class FotosInline(admin.ModelAdmin):
    model = Fotos
    extra = 1
    fields = ('imagen')

class CurriculumInline(admin.ModelAdmin):
    model = Curriculum
    extra = 1
    fields = ('archivo')

class DemoInline(admin.ModelAdmin):
    model = Demo
    fields = 'video'

class SocialInline(admin.ModelAdmin):
    model = Social
    extra = 1
    fields = ('facebook', 'instagram', 'twitter', 'tiktok')

class ActorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'foto', 'biografia')
    search_fields = ('nombre')
    inlines = [SeriesInline, PeliculasInline, TelevisionInline, FotosInline, CurriculumInline, DemoInline, SocialInline]


admin.site.register(Actor, ActorAdmin)