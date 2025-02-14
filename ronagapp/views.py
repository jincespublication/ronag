from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    team = Team.objects.all()
    context = {'teams': team}
    return render(request, 'about.html', context)

def contact(request):
    return render(request, 'contact.html')

def news(request):
    return render(request, 'news.html')

def singleNews(request):
    return render(request, 'singleNews.html')

def singleProduct(request):
    return render(request, 'singleProduct.html')