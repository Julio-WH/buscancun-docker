from django.shortcuts import render

# Create your views here.


def lista_choferes(request):
    context = {'test': 'Julio Eduardo'}
    return render(request, 'lista_choferes.html', context)