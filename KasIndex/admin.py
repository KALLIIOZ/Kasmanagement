from django.contrib import admin
from .models import Actor, Serie, Pelicula, Television, Foto, Curriculum, Demo, Social, Client, Icon

# Register your models here.

class SeriesInline(admin.StackedInline):
    model = Serie
    extra = 1
    fields = ('nombre', 'portada', 'plataforma',)

class PeliculasInline(admin.StackedInline):
    model = Pelicula
    extra = 1
    fields = ('nombre', 'portada', 'plataforma',)

class TelevisionInline(admin.StackedInline):
    model = Television
    extra = 1
    fields = ('nombre', 'portada', 'televisora',)

class FotosInline(admin.StackedInline):
    model = Foto
    extra = 1
    fields = ('imagen',)

class CurriculumInline(admin.StackedInline):
    model = Curriculum
    extra = 1
    fields = ('archivo',)

class DemoInline(admin.StackedInline):
    model = Demo
    extra = 1
    fields = ('video',)

class SocialInline(admin.StackedInline):
    model = Social
    extra = 1
    fields = ('facebook', 'instagram', 'twitter', 'tiktok',)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'foto', 'biografia', 'especial',)
    search_fields = ('nombre',)
    inlines = [SeriesInline, PeliculasInline, TelevisionInline, FotosInline, CurriculumInline, DemoInline, SocialInline]

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'foto',)

class IconsAdmin(admin.ModelAdmin):
    list_display = ('nombre','foto',)


admin.site.register(Actor, ActorAdmin)
admin.site.register(Client, ClientsAdmin)
admin.site.register(Icon, IconsAdmin)