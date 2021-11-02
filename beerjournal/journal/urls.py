from django.urls import path
from . import views

app_name = 'journal'
urlpatterns = [
    path('', views.index, name='index'),
    path('beers/', views.beers, name='beers'),
    path('beers/<int:beer_id>/', views.beer, name='beer'),
    path('beers/new/', views.new_beer, name='new_beer'),
    path('entry/new/<int:beer_id>/', views.new_entry, name='new_entry'),
    path('entry/edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]