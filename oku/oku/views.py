__author__ = 'NAV3'
 # -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
#import geometry
from models import *
from django.shortcuts import render_to_response
def Dest(request):
    destinations = Destinations.objects.all()
    #print destinations
    return render_to_response('merhaba.html', {'destinations':destinations, 'selam':'dunya'})

def search(request):
    if 'q' in request.GET:
        destinations = Destinations.objects.filter(cityname__contains = request.GET['q'])
        return render_to_response('merhaba.html', {'destinations':destinations, 'selam':'dunya'})
        #message = 'You searched for:%r' %(request.GET['q'])
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)

'''def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for:%r' %(request.GET['q'])
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
#def geosearch(request):'''






