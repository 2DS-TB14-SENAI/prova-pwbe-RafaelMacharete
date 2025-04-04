from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def criar_listar_servicos(req, pk=None):
    if req.method == 'GET':
        if pk:
            try:
                servico = Servico.objects.get(pk=pk)
            except Servico.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            servico = Servico.objects.all()

        servico_serializer = ServicoSerializer(servico, many=True)
        return Response(servico_serializer.data, status=status.HTTP_200_OK)

    elif req.method == 'POST':
        servicos_serializer = ServicoSerializer(data=req.data)
        if servicos_serializer.is_valid():
            servicos_serializer.save()
            return Response(servicos_serializer.data, status=status.HTTP_201_CREATED)

        return Response(servicos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def criar_listar_agendamentos(req, pk=None):
    if req.method == 'GET':
        
        if pk:
            
            try:
                agendamento = Agendamento.objects.get(pk=pk)
                agendamento_serializer = AgendamentoSerializer(agendamento)
            except Agendamento.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            agendamento = Agendamento.objects.all()
            agendamento_serializer = AgendamentoSerializer(agendamento, many=True)
        
        return Response(agendamento_serializer.data, status=status.HTTP_200_OK)

    elif req.method == 'POST':
        agendamentos_serializer = AgendamentoSerializer(data=req.data)
        if agendamentos_serializer.is_valid():
            agendamentos_serializer.save()
            return Response(agendamentos_serializer.data, status=status.HTTP_201_CREATED)

        return Response(agendamentos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)