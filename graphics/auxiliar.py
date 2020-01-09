from django.shortcuts import render

#Mostrar mensajes en pantalla
from django.contrib import messages

#Graficar datos
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

#Models
from DASE.models import beca_excelencia
from django.db.models import Sum

#Nuevas
import io
from django.http import HttpResponse


def f(request):

 if request.method == 'POST':
        
        #PIDIENDO Y GUARDANDO DATOS A GRAFICAR
        #x, y = buscar_datos()

        #Creamos una figura y le dibujamos el gráfico
        f = plt.figure()

        #Configurando el diseño del grafico
        plt.pie(x, labels=y, autopct="%0.1f %%")
        plt.axis("equal")
        #plt.show()

        #Como enviaremos la imagen en bytes la guardaremos en un buffer
        buf = io.BytesIO()
        canvas = FigureCanvasAgg(f)
        canvas.print_png(buf)

        #Creamos la respuesta enviando los bytes en tipo imagen png
        response = HttpResponse(buf.getvalue(), content_type='image/png')

        #Limpiamos la figura para liberar memoria
        f.clear()

        #Añadimos la cabecera de longitud de fichero para más estabilidad
        response['Content-Length'] = str(len(response.content))

        #Devolvemos la response
        return render(request, 'graficas.html', {"r":response})
        #return response
     else:
        #buscar_datos()
        return render(request, 'google.html', {'values': [['foo', 32], ['bar', 64], ['baz', 96]] })