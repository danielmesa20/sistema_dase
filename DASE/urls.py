from django.urls import path
from DASE.views import import_excel, busqueda

urlpatterns = [
    path('import', import_excel, name="import"),
    path('busqueda', busqueda, name="busqueda"),
]
