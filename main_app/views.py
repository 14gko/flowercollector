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
    flowers = Flower.objects.all()
    return render(request, 'flowers/index.html', { 'flowers': flowers })