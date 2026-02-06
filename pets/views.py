from django.shortcuts import render
from .forms import ServiceForm, PetForm
from .models import Service, Pet

def pet_list(request):
    return render(request, 
                  '/pets.html',
                  {'pets': Pet.objects.all()})

def create_service(request):
    return render(request, 
                  '/service.html',
                  {"service": ServiceForm()})