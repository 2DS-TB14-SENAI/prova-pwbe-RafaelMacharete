from django.urls import path
from . import views

urlpatterns = [
    path('api/servicos/', views.criar_listar_servicos, name='listar_servicos'),
    path('api/servicos/', views.criar_listar_servicos, name='criar_servico'),
    path('api/servicos/<int:pk>', views.criar_listar_servicos, name='criar_consulta'),

    path('api/agendamentos/', views.criar_listar_agendamentos, name='listar_servicos'),
    path('api/agendamentos/', views.criar_listar_agendamentos, name='criar_servico'),
    path('api/agendamentos/<int:pk>/', views.criar_listar_agendamentos, name='criar_consulta'),
]
