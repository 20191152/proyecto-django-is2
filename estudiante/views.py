from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializer import EstudianteSerializer
from .models import Estudiante
from .form import RegistroEstudianteForm

class EstudianteViewSet(viewsets.ModelViewSet):
    serializer_class = EstudianteSerializer
    queryset = Estudiante.objects.all()

def signup_estudiante(request):
    if request.method == 'POST':
        form = RegistroEstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            codigo = form.cleaned_data.get('codigo')
            password = form.cleaned_data.get('password1')
            user = authenticate(codigo=codigo, password=password)
            login(request, user)
            return redirect('inicio_estudiante')
        else:
            return render(request, 'signup_estudiante.html', {'form': form, 'error': 'Datos no válidos. Intente nuevamente.'})
    else:
        form = RegistroEstudianteForm()
    return render(request, 'signup_estudiante.html', {'form': form})

def inicio_estudiante(request):
    return render(request, 'inicio_estudiante.html')

def buscar_curso(request):
    from curso.models import Curso
    cursos = Curso.objects.all()
    paginator = Paginator(cursos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'buscar_cursos.html', {'page_obj': page_obj})

def mis_cursos(request):
    return render(request, 'cursos_estudiante.html')

def mi_perfil(request):
    estudiante = request.user.estudiante
    return render(request, 'perfil_estudiante.html', {'estudiante': estudiante})

def editar_perfil(request):
    estudiante = request.user.estudiante
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        if nombre and apellido and email:
            estudiante.nombre = nombre
            estudiante.apellido = apellido
            estudiante.email = email
            estudiante.save()
            return redirect('perfil_estudiante')
        else:
            return render(request, 'editar_perfil_estudiante.html', {'error': 'Datos no válidos. Intente nuevamente.'})
    return render(request, 'editar_perfil_estudiante.html', {'estudiante': estudiante})

def actualizar_perfil(request):
    estudiante = request.user.estudiante
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        if nombre and apellido and email:
            estudiante.nombre = nombre
            estudiante.apellido = apellido
            estudiante.email = email
            estudiante.save()
            return redirect('perfil_estudiante')
        else:
            return render(request, 'perfil_estudiante.html', {'error': 'Datos no válidos. Intente nuevamente.'})
    return redirect('perfil_estudiante')