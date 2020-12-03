from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='travel-home'),
    path('nearby',views.nearbylocations, name='nearby_location')
]