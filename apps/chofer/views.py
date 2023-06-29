from django.shortcuts import render
from apps.chofer.models import Chofer, Autobus
from django.core import serializers
# Create your views here.
import time

def lista_choferes(request):
    choferes = Chofer.objects.all()
    context = {'choferes': choferes}
    return render(request, 'lista_choferes.html', context)

def get_autobuses():
    time.sleep(10)
    autobuses = Autobus.objects.all()
    data = serializers.serialize('json', autobuses)
    return data
