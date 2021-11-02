from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Beer, Entry
from .forms import BeerForm, EntryForm

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'journal/index.html')

@login_required
def beers(request):
    beers = Beer.objects.filter(owner=request.user).order_by('date_added')    
    context = {'beers':beers}
    return render(request, 'journal/beers.html', context)

@login_required
def beer(request, beer_id):
    beer = Beer.objects.get(id=beer_id)

    if beer.owner != request.user:
        raise Http404

    entries = beer.entry_set.order_by('-date_added')
    context = {'beer':beer, 'entries':entries}
    return render(request, 'journal/beer.html', context)

@login_required
def new_beer(request):
    if request.method != 'POST':
        form = BeerForm()
    else:
        form = BeerForm(data=request.POST)
        if form.is_valid():
            new_beer = form.save(commit=False)
            new_beer.owner = request.user
            new_beer.save()
            return redirect('journal:beers')

    context = {'form':form}    
    return render(request, 'journal/new_beer.html', context)

@login_required
def new_entry(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # Grab the data
            new_entry.beer = beer #Set attribute before saving
            new_entry.save() #Save
            return redirect('journal:beer', beer_id=beer_id)
    context = {'beer':beer, 'form':form}
    return render(request, 'journal/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    beer = entry.beer

    if beer.owner != request.user:
        raise Http404    

    if request.method != 'POST':
        form = EntryForm(instance=entry)    
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal:beer', beer_id = beer.id)
    context = {'entry':entry, 'beer':beer, 'form':form}
    return render(request, 'journal/edit_entry.html', context)