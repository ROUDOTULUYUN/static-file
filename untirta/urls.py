from django.contrib import admin
from django.urls import path
from faperta.views import prodi1
from feb.views import prodi3
from fh.views import prodi4
from fisip.views import prodi5
from fk.views import prodi6
from fkip.views import prodi7
from ft.views import prodi8
from pascasarjana.views import prodi9

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', prodi1),
    path('feb/', prodi3),
    path('fh/', prodi4),
    path('fisip/', prodi5),
    path('fk/', prodi6),
    path('fkip/', prodi7),
    path('ft/', prodi8),
    path('pascasarjana/', prodi9),
    
]
