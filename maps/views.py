from django.shortcuts import render
from . import models

def mapa_puntos_interes(request):
    allParsedPlaces = []

    placesInDb = models.InterestLocation.objects.all()
    for place in placesInDb:
        parsedPlace = {
            "name": place.nombre,
            "comuna": place.comuna,
            "type": place.tipo,
            "custom_relevantes": [place.encontrables],#place.location_things,
            "custom_razonvisita": [place.razonvisita], #place.location_name,
            "lat": place.latitud,
            "lng": place.longitud,
        }

        allParsedPlaces.append(parsedPlace)

    zones = []
    return render(request, "maps/v_puntosinteres.html", {"places": allParsedPlaces, "zones": zones})

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

    return render(request, "maps/v_agregarpuntointeres.html", {"places": places, "zones": zones})