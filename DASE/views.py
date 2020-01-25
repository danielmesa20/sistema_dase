from django.shortcuts import render

# Usar objectos "Q"
from django.db.models import Q


# Mostrar mensajes en pantalla
from django.contrib import messages


# Models
from DASE.models import estudiantes, indices

# Verificacion de datos del excel
import math

#Verificar que el usuario esta logueado
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'login.html')


@login_required
def busqueda(request):

    # Query para solicitar los valores que contendran  los select
    c = estudiantes.objects.values('carrera').distinct()
    b = estudiantes.objects.values('tipo_beneficio').distinct()
    # t = estudiantes.objects.values('trimestre').distinct()

    if request.method == 'POST':

        # Recuperar los valores ingresados
        input_text = request.POST['data']
        s1 = request.POST.getlist('select_carrera')
        s2 = request.POST.getlist('select_beneficio')
        # s3 = request.POST.getlist('select_trimestre')
        s4 = request.POST['select_order']

        # Criterios de busqueda
        lista = []

        # Inicializando variable donde se guardará el query
        query = Q()

        # Construcción del query a partir de las opciones ingresadas por el usuario

        if (input_text):
            for i in input_text.split(" "):
                if (i.isdigit()):
                    query |= Q(cedula=i)
                elif (not i.isdigit() and i != ''):
                    query |= Q(nombre__icontains=i)
                lista.append(i)

        if (s1):
            query &= Q(carrera__in=s1)
            lista.append(", ".join(s1))
        if (s2):
            query &= Q(tipo_beneficio__in=s2)
            lista.append(", ".join(s2))
        # if (s3):
        #     query &= Q(trimestre__in=s3)

        # Solicitando los datos a la base de datos
        if(s4):
            datos = estudiantes.objects.values('nombre','cedula','tipo_beneficio','carrera').filter(query).order_by(s4)
        else:
            datos = estudiantes.objects.values('nombre','cedula','tipo_beneficio','carrera').filter(query).order_by("cedula")

        for i in lista:
            if i == '':
                lista.remove(i)

        print(lista)

        # Si no se encentran resultados se muestra un mensaje al usuario
        if not datos:
            messages.info(
                request, "No hay resultados que coincidan con su búsqueda: %s " % (', '.join(lista)))

        return render(request, 'busqueda.html', {"c": c, "b": b, "search": datos})

    else:
        return render(request, 'busqueda.html', {"c": c, "b": b})


from django.contrib.auth.decorators import login_required


@login_required
def more_info(request, cedula):

    # Busca toda la información relacionada con el estudiante solicitado
    #estudiante = estudiantes.objects.filter(cedula=cedula)
    student_test = indices.objects.select_related(
         'cedula_fk').filter(cedula_fk=cedula) #.values('iaa','iap','trimestre')

    #print(str(estudiante_test.query))
    #print(estudiante_test[0].cedula_fk.nombre)
    #print(estudiante_test.cedula_fk.nombre)

    n  =  student_test[0].cedula_fk.nombre
    c  =  student_test[0].cedula_fk.cedula
    b  =  student_test[0].cedula_fk.cedula
    cr = student_test[0].cedula_fk.carrera
    
    # for i in estudiante_test:
    #    print(i.cedula_fk.nombre)

    return render(request, 'more_info.html', {"name": n, "cedula": c, "beneficio":b, "carrera":cr, "indices": student_test })
