from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def REGISTER(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Nombre de usuario ya existe')
                return redirect("REGISTER")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Ese email ya está registrado')
                return redirect('REGISTER')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'Usuario creado correctamente')
                return redirect('LOGIN')
        else:
            messages.info(request, 'Las contraseñas no coinciden')
            return redirect('REGISTER')
    else:
        return render(request, 'register.html')


def LOGIN(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            messages.info(request, "Error en las credenciales")
            return redirect("LOGIN")
    else:
        return render(request, 'login.html')


def LOGOUT(request):
    auth.logout(request)
    return render(request, 'home.html')
