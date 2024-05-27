from django.shortcuts import render, get_object_or_404, redirect
from .models import Empregado
from .forms import EmpregadoForm

from rest_framework import viewsets
from .serializers import EmpregadoSerializer

from django.db.models import Q

from django.core.paginator import Paginator

def feed_empregados(request):
    empregados = Empregado.objects.all()
    cargos = Empregado.objects.values_list('cargo', flat=True).distinct()
    
    query = request.GET.get('search')
    sort_by = request.GET.get('sort_by', 'nome')  # Default sort field is 'nome'
    filter_by = request.GET.get('filter_by', None)  # Default filter field is None
    
    if query:
        empregados_list = Empregado.objects.filter(Q(nome__icontains=query))
    else:
        empregados_list = Empregado.objects.all()
    
    if filter_by:
        empregados_list = empregados_list.filter(cargo=filter_by)

    empregados_list = empregados_list.order_by(sort_by)
    
        
    # Pagination Code    
    paginator = Paginator(empregados_list, 4)  # Show 10 empregados per page.
    page_number = request.GET.get('page')
    empregados = paginator.get_page(page_number)
    
    return render(request, 'empregados/feed_empregados.html', {'empregados': empregados, 'cargos': cargos})


def lista_empregados(request):
    empregados = Empregado.objects.all()
    cargos = Empregado.objects.values_list('cargo', flat=True).distinct()
    
    query = request.GET.get('search')
    sort_by = request.GET.get('sort_by', 'nome')  # Default sort field is 'nome'
    filter_by = request.GET.get('filter_by', None)  # Default filter field is None
    
    if query:
        empregados_list = Empregado.objects.filter(Q(nome__icontains=query))
    else:
        empregados_list = Empregado.objects.all()
    
    if filter_by:
        empregados_list = empregados_list.filter(cargo=filter_by)

    empregados_list = empregados_list.order_by(sort_by)
    
        
    # Pagination Code    
    paginator = Paginator(empregados_list, 4)  # Show 10 empregados per page.
    page_number = request.GET.get('page')
    empregados = paginator.get_page(page_number)
    
    return render(request, 'empregados/lista_empregados.html', {'empregados': empregados, 'cargos': cargos})

def criar_empregado(request):
    if request.method == 'POST':
        form = EmpregadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empregados')
    else:
        form = EmpregadoForm()
    return render(request, 'empregados/form_empregado.html', {'form': form})

def editar_empregado(request, pk):
    empregado = get_object_or_404(Empregado, pk=pk)
    if request.method == 'POST':
        form = EmpregadoForm(request.POST, instance=empregado)
        if form.is_valid():
            form.save()
            return redirect('lista_empregados')
    else:
        form = EmpregadoForm(instance=empregado)
    return render(request, 'empregados/form_empregado.html', {'form': form})

def deletar_empregado(request, pk):
    empregado = get_object_or_404(Empregado, pk=pk)
    if request.method == 'POST':
        empregado.delete()
        return redirect('lista_empregados')
    return render(request, 'empregados/confirmar_delecao.html', {'empregado': empregado})

def detalhe_empregado(request, pk):
    empregado = get_object_or_404(Empregado, pk=pk)
    return render(request, 'empregados/detalhe_empregado.html', {'empregado': empregado})

class EmpregadoViewSet(viewsets.ModelViewSet):
    queryset = Empregado.objects.all()
    serializer_class = EmpregadoSerializer
