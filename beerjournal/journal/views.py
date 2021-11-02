from django.shortcuts import render, redirect
from .models import Beer
from .forms import BeerForm

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

def new_beer(request):
    if request.method != 'POST':
        form = BeerForm()
    else:
        form = BeerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal:beers')

    context = {'form':form}    
    return render(request, 'journal/new_beer.html', context)