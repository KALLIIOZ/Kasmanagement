from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns=[
    path('', views.index_view, name='index'),
    path('actor/<str:nombre>/', views.actor_detail, name='actor_perfil'),
    path('contact/', views.contact, name='contact_us')
]