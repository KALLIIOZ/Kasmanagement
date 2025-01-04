from django.contrib import admin
from .models import Actor, Series, Peliculas, Television, Fotos, Curriculum, Demo, Social

# Register your models here.

class SeriesInline(admin.TabularInline):
    model = Series
    extra = 1
    fields = ('nombre', 'portada', 'plataforma',)

class PeliculasInline(admin.TabularInline):
    model = Peliculas
    extra = 1
    fields = ('nombre', 'portada', 'plataforma',)

class TelevisionInline(admin.TabularInline):
    model = Television
    extra = 1
    fields = ('nombre', 'portada', 'televisora',)

class FotosInline(admin.TabularInline):
    model = Fotos
    extra = 1
    fields = ('imagen',)

class CurriculumInline(admin.TabularInline):
    model = Curriculum
    extra = 1
    fields = ('archivo',)

class DemoInline(admin.TabularInline):
    model = Demo
    fields = ('video',)

class SocialInline(admin.TabularInline):
    model = Social
    extra = 1
    fields = ('facebook', 'instagram', 'twitter', 'tiktok',)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'foto', 'biografia', 'especial',)
    search_fields = ('nombre',)
    inlines = [SeriesInline, PeliculasInline, TelevisionInline, FotosInline, CurriculumInline, DemoInline, SocialInline]


admin.site.register(Actor, ActorAdmin)