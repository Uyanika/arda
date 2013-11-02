
# Create your views here.
from django.http import *
from models import *
from django.shortcuts import render_to_response
def Dest(request):
    Dest = Destinations.objects.all()
    return render_to_response('pgshtml.html', Dest)
