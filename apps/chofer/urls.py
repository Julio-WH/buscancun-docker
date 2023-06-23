# Django imports
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from apps.chofer.views import lista_choferes

urlpatterns = [
    path('lista/', lista_choferes, name='lista_choferes'),
]