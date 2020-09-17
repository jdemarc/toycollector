from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Plant
from .forms import WateringForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello.</h1>')

def about(request):
  return render(request, 'about.html')

def plants_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html', {'plants': plants})

def plants_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  watering_form = WateringForm()
  return render(request, 'plants/detail.html', {'plant': plant, 'watering_form': watering_form})

def add_watering(request, plant_id):
  form = WateringForm(request.POST)
  if form.is_valid():
    new_watering = form.save(commit=False)
    new_watering.plant_id = plant_id
    new_watering.save()
  return redirect('detail', plant_id=plant_id)

class PlantCreate(CreateView):
  model = Plant
  fields = '__all__'
  success_url = '/plants/'

class PlantUpdate(UpdateView):
  model = Plant
  fields = '__all__'
  # fields = ['name', 'description', 'age']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'