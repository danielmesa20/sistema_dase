from django.shortcuts import render
import pandas as pd
from sqlalchemy import create_engine, exc
from django.conf import settings
from django.contrib import messages
from DASE.models import beca_excelencia

# Create your views here.

def  import_excel (request):

    if request.method == 'POST' and request.FILES['excel']:
        
        #CREDENCIALES DATABASE
        #engine = create_engine('postgresql://postgres:password@localhost:5432/base_tesis_2')
       
        #IMPORTANDO ARCHIVO EXCEL
        excel = request.FILES['excel']

        #LEYENDO TODAS LAS HOJAS DEL EXCEL
        data = pd.read_excel(excel, sheet_name='p2')
        #data = pd.read_excel(excel, sheet_name='p2', usecols=['cedula'])
        #print(data['cedula'][0])

        contador=0
        for i in data['cedula']:
            prueba = beca_excelencia(cedula=data['cedula'][contador], nombre=data['nombre'][contador])
            prueba.save()
            contador = contador + 1   

        # #GUARDAR DATOS EN LA DATABASE
        # for i in data:
        #     if i == "p1":
        #         data[i].to_sql(name='beca_excelencia', con=engine, if_exists='append')
        #         print("no")
        #     else:
        #         prueba = beca_excelencia(cedula=data['cedula'])
        #         prueba.save()
        #         try:
        #             data[i].to_sql(name='DASE_beca_excelencia_test2', con=engine, if_exists='append')

        #         except exc.DBAPIError as ex:    
        #             messages.info(request, "Error: %s en la hoja: %s, la información de esa hoja no fue importada a la BD " %(ex.orig.diag.message_primary, i) )
        #             messages.info(request, "Revise el documento excel y vuelva a cargar  el archivo para importar la información faltante")
        #         print("si")
                
    return render(request, 'test.html')

def graficas(request):
    # data = Productos.objects.all()
    # products= Productos.objects.filter(categoria="Base")
    return 1