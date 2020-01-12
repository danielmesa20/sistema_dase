from django.urls import path
from DASE.views import import_excel, busqueda, more_info

urlpatterns = [
    path('import', import_excel, name="import"),
    path('busqueda', busqueda, name="busqueda"),
    path('more_info/<int:cedula>', more_info, name="more_info"),
]
