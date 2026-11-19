from django.shortcuts import render, redirect
from . import models
from .forms import InterestLocationForm
from .models import InterestLocation
from django.core.exceptions import PermissionDenied, ValidationError

def mapa_puntos_interes(request):
    allParsedPlaces = []

    zones = []
    placesInDb = models.InterestLocation.objects.all()

    for place in placesInDb:
        parsedPlace = {
            "name": place.nombre,
            "comuna": place.comuna,
            "tipo": place.tipo,
            "custom_relevantes": [place.encontrables],#place.location_things,
            "custom_razonvisita": [place.razonvisita], #place.location_name,
            "lat": place.latitud,
            "lng": place.longitud,
        }

        allParsedPlaces.append(parsedPlace)

    usuario = request.user
    is_curator = usuario.is_authenticated and usuario.has_perm('maps.can_create_location')

    return render(request, "maps/v_puntosinteres.html", {"places": allParsedPlaces, "zones": zones, "is_curator": is_curator})

def mapa_riesgo_zonas(request):
    places = []
    zones = [
        {
            "name": "feik providencia",

            "custom_riesgo": "Riesgo Alto",
            "custom_razonriesgo": ["Razon numero 1", "Razon numero 2", "La tercera"],

            "points": [
                [-33.456164359260136, -70.62557602243034],
                [-33.46361139802507, -70.60085678414909],
                [-33.45032085089647, -70.59641075291438],
                [-33.442987262227966, -70.60789490060417],
            ]
        }
    ]
    return render(request, "maps/v_riesgozonas.html", {"places": places, "zones": zones})

def agregar_punto_interes(request):
    places = []
    zones = []

    if request.method == 'POST':
        form = InterestLocationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            InterestLocation.objects.create(
                nombre=data['add_lugar_nombre'],
                comuna=data['add_lugar_comuna'],
                tipo=data['add_lugar_tipo'],
                encontrables=data['add_lugar_encontrar'],
                razonvisita=data['add_lugar_razon'],
                latitud=data['lat'],
                longitud=data['lng'],
            )
            return redirect('maps:puntosinteres')
    else:
        form = InterestLocationForm()

    usuario = request.user
    is_curator = usuario.is_authenticated and usuario.has_perm('maps.can_create_location')

    if not is_curator:
        raise PermissionDenied()

    return render(request, 'maps/v_agregarpuntointeres.html', {'form': form, "places": places, "zones": zones, "is_curator": is_curator})