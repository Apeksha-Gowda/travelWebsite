from django.urls import path
#from .views import calculate_distance_view
from . import views
app_name = 'distance'

urlpatterns = [
    path('distance/',views.calculate_distance_view, name='calculate-view'),
]