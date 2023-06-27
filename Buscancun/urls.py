from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from apps.sistema.index import IndexHomeView, index_home_view

urlpatterns = [
    path('', index_home_view, name="index_home"),
    url(r'^admin/', admin.site.urls),
    path('chofer/', include('apps.chofer.urls')),
]
