from django.urls import path
from . import views

app_name = "maps"

urlpatterns = [
    path("mapa/puntosinteres", views.mapa_puntos_interes, name="puntosinteres"),
    path("mapa/riesgozonas", views.mapa_riesgo_zonas, name="riesgozonas"),
]