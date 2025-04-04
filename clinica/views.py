from django.shortcuts import render, redirect, get_object_or_404

from .models import Medico, Consulta
from .serializers import ConsultaSerializer, MedicoSerializer
from .forms import ConsultaForm

def index(req):
    return render(req, 'clinica/base.html')

def listar_medicos(req):
    if req.method == 'GET':
        todos_medicos = Medico.objects.all()
        return render(req, 'clinica/listar_medicos.html', {'todos_medicos': todos_medicos})
    if req.method == 'POST':
        procurado = req.POST['search']
        medicos_filtrados = Medico.objects.filter(nome__icontains=procurado)
        return render(
            req,
            'clinica/listar_medicos.html',
            {
             'procurado': procurado,
             'medicos_filtrados': medicos_filtrados
            })

def criar_consulta(req):
    if req.method == 'POST':
        form = ConsultaForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos') # trocar isso aqui
    else:
        form = ConsultaForm()

    return render(req, 'clinica/form_consulta.html', {'form': form})

def detalhes_consulta(req, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    return render(req, 'clinica/detalhes_consulta.html', {'consulta': consulta})