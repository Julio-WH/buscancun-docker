from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from apps.sistema.index import IndexHomeView, index_home_view, VueView

urlpatterns = [
    path('', index_home_view, name="index_home"),
    path('vue/', VueView.as_view(), name='vue'),
    url(r'^admin/', admin.site.urls),
    path('chofer/', include('apps.chofer.urls')),
]
