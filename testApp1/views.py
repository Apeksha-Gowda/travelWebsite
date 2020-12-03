from django.shortcuts import render
from .models import Destinations
from django.contrib.auth.decorators import login_required
from .filters import DestinationsFilter

@login_required
def home(request):
    destination = Destinations.objects.all()
    myFilter = DestinationsFilter(request.GET, queryset = destination)
    destination  = myFilter.qs
    context = {
        'destinations' : destination,
        'myFilter' : myFilter
    }
    return render(request,'testApp1/home.html', context)

def portfolio(request):
    if request.method == 'GET':
        destination_id = request.GET.get('destination_id')
        values = Destinations.objects.get(id=destination_id)
        
    context = {
        "values":values,
    }
   
    return render(request,'testApp1/portfolio.html', context)

