from django.urls import path
from .views import *

urlpatterns = [

    path("", user_login, name="login"),
    path("inicio/", inicio, name="inicio"),
    path("logout/", logout_view, name="logout"),
    path("tjson/", json_todo, name="json"),
    path("csv/", csv_exportacion, name="csv"),
    # ClienteView URLs
    path('clientes/', ClienteView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteView.as_view(), name='cliente-detail-update'),

    # MascotaView URLs
    path('mascotas/', MascotaView.as_view(), name='mascota-list-create'),
    path('mascotas/<int:pk>/', MascotaView.as_view(), name='mascota-detail-update'),

    path("mascota/tabla", getMascota, name="mascotas"),
    path("mascota/nuevo", addMascota, name="nueva-mascota"),
    path("mascota/actualizar/<int:id>", upMascota, name="actualizar-mascota"),
    path("mascota/eliminar/<int:id>", eliminar_mascota, name="eliminar-mascota"),

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

    path("veterinario/tabla", getVeterinario, name="veterinarios"),
    path("veterinario/nuevo", addVeterinario, name="nuevo-veterinario"),
    path("veterinario/actualizar/<int:id>", upVeterinario, name="actualizar-veterinario"),
    path("veterinario/eliminar/<int:id>", eliminar_Veterinario, name="eliminar-veterinario"),

    # MedicamentoView URLs
    path('medicamentos/', MedicamentoView.as_view(), name='medicamento-list-create'),
    path('medicamentos/<int:pk>/', MedicamentoView.as_view(), name='medicamento-detail-update'),

]