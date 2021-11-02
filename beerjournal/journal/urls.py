from django.urls import path
from . import views

app_name = 'journal'
urlpatterns = [
    path('', views.index, name='index'),
    path('beers/', views.beers, name='beers'),
    path('beers/<int:beer_id>/', views.beer, name='beer'),
]