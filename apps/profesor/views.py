from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework import viewsets
from .factories import CursoConcreteFactory
from .serializer import ProfesorSerializer
from .models import Profesor
from .form import RegistroProfesorForm

class ProfesorViewSet(viewsets.ModelViewSet):
    serializer_class = ProfesorSerializer
    queryset = Profesor.objects.all()

def signup_profesor(request):
    if request.method == 'POST':
        form = RegistroProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            codigo = form.cleaned_data.get('codigo')
            password = form.cleaned_data.get('password1')
            user = authenticate(codigo=codigo, password=password)
            login(request, user)
            return redirect('inicio_profesor')
        else:
            return render(request, 'profesor/signup_profesor.html', {'form': form, 'error': 'Datos no válidos. Intente nuevamente.'})
    else:
        form = RegistroProfesorForm()
    return render(request, 'profesor/signup_profesor.html', {'form': form})

@login_required
def inicio_profesor(request):
    return render(request, 'profesor/inicio_profesor.html')

@login_required
def mis_cursos(request):
    from apps.curso.models import Curso
    cursos = Curso.objects.filter(profesor=request.user.profesor).order_by('ultima_modificacion')
    if not cursos:
        return render(request, 'profesor/cursos_profesor.html')
    paginator = Paginator(cursos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'profesor/cursos_profesor.html', {'page_obj': page_obj})

@login_required
def crear_curso(request):
    factory = CursoConcreteFactory()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        categoria = request.POST.get('categoria')
        nivel = request.POST.get('nivel')
        profesor = request.user.profesor
        # Crear curso
        curso = factory.create_curso(nombre=nombre, descripcion=descripcion, categoria=categoria, nivel=nivel, profesor=profesor)
        if curso:
            return redirect('cursos_profesor')
        return render(request, 'profesor/crear_curso.html', {'error2': 'Datos no válidos. Intente nuevamente.'})
    return render(request, 'profesor/crear_curso.html')

@login_required
def crear_seccion(request, curso_id):
    factory = CursoConcreteFactory()
    if request.method == 'POST':
        from apps.curso.models import Curso
        curso = Curso.objects.get(id=curso_id)
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        # Crear sección
        seccion = factory.create_seccion(curso=curso, nombre=nombre, descripcion=descripcion)
        if seccion:
            return redirect('detalle_curso', curso_id=curso.id)
        return render(request, 'profesor/crear_seccion.html', {'error': 'Datos no válidos. Intente nuevamente.', 'curso': curso})
    return render(request, 'profesor/crear_seccion.html', {'curso': curso})

@login_required
def detalle_curso(request, curso_id):
    from apps.curso.models import Curso
    curso = get_object_or_404(Curso, id=curso_id)
    secciones = curso.seccion_set.all()
    return render(request, 'profesor/detalle_curso.html', {'curso': curso, 'secciones': secciones})