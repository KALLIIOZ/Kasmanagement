from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'KasIndex/index.html')

def actor_view(request):
    return render(request, 'KasIndex/actor.html')

def contact_view(request):
    return render(request, 'KasIndex/contact_us.html')