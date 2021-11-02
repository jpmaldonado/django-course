from django.shortcuts import render
from .models import Beer

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'journal/index.html')

def beers(request):
    beers = Beer.objects.order_by('date_added')    
    context = {'beers':beers}
    return render(request, 'journal/beers.html', context)


def beer(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    entries = beer.entry_set.order_by('-date_added')
    context = {'beer':beer, 'entries':entries}
    return render(request, 'journal/beer.html', context)