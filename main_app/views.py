from django.shortcuts import render, redirect
# add this import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Flower, Fertilizer
from .forms import WateringForm

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def flowers_index(request):
    flowers = Flower.objects.order_by('name')
    return render(request, 'flowers/index.html', { 'flowers': flowers })

def flowers_detail(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    # get fertilizers that this flower doesnt user
    id_list = flower.fertilizers.all().values_list('id')
    # now filter this list
    unused_fert = Fertilizer.objects.exclude(id__in=id_list)
    # instantiate wateringform to be rendered in template
    watering_form = WateringForm()
    return render(request, 'flowers/detail.html', { 
            'flower': flower, 
            'watering_form': watering_form,
            'fertilizers': unused_fert
            })

def add_watering(request, flower_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.flower_id = flower_id
        new_watering.save()
    return redirect('detail', flower_id=flower_id)

def assoc_fert(request, flower_id, fertilizer_id):
    Flower.objects.get(id=flower_id).fertilizers.add(fertilizer_id)
    return redirect('detail', flower_id=flower_id)

class FlowerCreate(CreateView):
    model = Flower
    fields = ['name', 'family', 'color', 'description', 'quantity']
    success_url = '/flowers/'

class FlowerUpdate(UpdateView):
    model = Flower
    fields = ['color', 'description', 'quantity']

class FlowerDelete(DeleteView):
    model = Flower
    success_url = '/flowers/'

class FertList(ListView):
    model = Fertilizer

class FertDetail(DetailView):
    model = Fertilizer

class FertCreate(CreateView):
    model = Fertilizer
    fields = '__all__'

class FertUpdate(UpdateView):
    model = Fertilizer
    fields = ['name', 'type']

class FertDelete(DeleteView):
    model = Fertilizer
    success_url = '/fertilizers/'