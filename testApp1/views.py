from django.shortcuts import render
from .models import Destinations
from django.contrib.auth.decorators import login_required
from .filters import DestinationsFilter
import requests
from urllib.parse import urlencode

@login_required
def home(request):
    destination = Destinations.objects.all().order_by("-hits")
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
        hitcount = values.hits
        hitcount = hitcount + 1
        values.hits = hitcount
        values.save()
        
    context = {
        "values":values,
    }
   
    return render(request,'testApp1/portfolio.html', context)

def nearbylocations(request):
    api_Key = "AIzaSyCWRZPar2BHNZNKEHG4o1kxAJSDZG-BlTc"
    if request.method == 'POST':
        location = request.POST.get('location')
        radius = request.POST.get('radius')
        keywords = request.POST.get('keywords')

        endpoint_geocode = f"https://maps.googleapis.com/maps/api/geocode/json"
        params_geocode = {"address":location,"key":api_Key}
        url_params_geocode  = urlencode(params_geocode)
        url_geocode = f"{endpoint_geocode}?{url_params_geocode}"
        r = requests.get(url_geocode)
        if r.status_code not in range(200,299):
            return{}
        latlng = {}
        try:
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass
        lat,lng = latlng.get("lat"),latlng.get("lng")

        places_endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

        params_nearby = {
        "key" : api_Key,
        "location" : f"{lat},{lng}",
        "radius" : radius,
        "keyword" : keywords
        }

        params_nearby_encoded = urlencode(params_nearby)
        places_url = f"{places_endpoint}?{params_nearby_encoded}"
        r2 = requests.get(places_url)
        results = r2.json()["results"]
        context = {"results" : results}
        for result in results:
            print(result['name'])
        return render(request,'testApp1/nearby.html', context)
    else:
        context = {}
        return render(request,'testApp1/nearby.html', context)

