from django.shortcuts import render
# add this import
from django.http import HttpResponse
from .models import Flower

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
    return render(request, 'flowers/detail.html', { 'flower': flower })