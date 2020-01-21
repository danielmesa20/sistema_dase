from django.urls import path
from authentication.views import LOGIN, LOGOUT, REGISTER

urlpatterns = [
    path("LOGIN", LOGIN, name="LOGIN"),
    path("LOGOUT", LOGOUT, name="LOGOUT"),
    path("REGISTER", REGISTER, name="REGISTER"),
]
