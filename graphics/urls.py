from django.urls import path
from graphics.views import graficas

urlpatterns = [
    path('graficas', graficas , name="graficas"),
]
