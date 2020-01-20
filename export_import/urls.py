from django.urls import path
from export_import.views import import_excel

urlpatterns = [
    path('import', import_excel, name="import"),
]
