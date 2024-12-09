from django.urls import path
from .views import *

urlpatterns = [
    # ClienteView URLs
    path('clientes/', ClienteView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteView.as_view(), name='cliente-detail-update'),

    # MascotaView URLs
    path('mascotas/', MascotaView.as_view(), name='mascota-list-create'),
    path('mascotas/<int:pk>/', MascotaView.as_view(), name='mascota-detail-update'),

    # ConsultaView URLs
    path("consultas/table", getConsultas, name = "consultas"),
    path("consultas/nueva", addConsulta, name = "nueva-consultas"),
    path("consultas/actualizar/<int:id>", upConsulta, name = "actualizar-consultas"),
    path("consultas/eliminar/<int:id>", eliminar_consultas, name = "eliminar-consultas"),

    path('consultas/', ConsultaView.as_view(), name='consulta-list-create'),
    path('consultas/<int:pk>/', ConsultaView.as_view(), name='consulta-detail-update'),

    # VeterinarioView URLs
    path('veterinarios/', VeterinarioView.as_view(), name='veterinario-list-create'),
    path('veterinarios/<int:pk>/', VeterinarioView.as_view(), name='veterinario-detail-update'),

    # MedicamentoView URLs
    path('medicamentos/', MedicamentoView.as_view(), name='medicamento-list-create'),
    path('medicamentos/<int:pk>/', MedicamentoView.as_view(), name='medicamento-detail-update'),
]