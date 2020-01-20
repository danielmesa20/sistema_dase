from django.urls import path
from DASE.views import busqueda, more_info

urlpatterns = [
    path('busqueda', busqueda, name="busqueda"),
    path('more_info/<int:cedula>', more_info, name="more_info"),
]
