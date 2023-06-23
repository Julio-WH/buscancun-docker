from django.shortcuts import render
from apps.chofer.models import Chofer
# Create your views here.


def lista_choferes(request):
    choferes = Chofer.objects.all()
    context = {'choferes': choferes}
    return render(request, 'lista_choferes.html', context)
