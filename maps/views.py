from django.shortcuts import render

def mapa_puntos_interes(request):
    places = [
        {
            "name": "USM San Joaquin",

            "custom_type": "Universidad",
            "custom_relevantes": ["Patrimonios", "Edificios", "Biblioteca"],
            "custom_razonvisita": ["Lugar de estudios", "Buena Universidad"],

            "lat": -33.49089371165112,
            "lng": -70.61913133268338,
        },
    ]

    zones = []
    return render(request, "maps/v_puntosinteres.html", {"places": places, "zones": zones})

def mapa_riesgo_zonas(request):
    places = []
    zones = [
        {
            "name": "zona1",

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