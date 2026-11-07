from django.shortcuts import render

def mapa_puntos_interes(request):
    places = [
        {
            "name": "USM San Joaquin",
            "comuna": "Santiago",

            "tipo": "Universidad",
            "custom_relevantes": ["Patrimonios", "Edificios", "Biblioteca"],
            "custom_razonvisita": ["Lugar de estudios", "Buena Universidad"],

            "lat": -33.49089371165112,
            "lng": -70.61913133268338,
        },

        {
            "name": "Ubicacion 2 - Prueba",
            "comuna": "Providencia",

            "tipo": "Lugar tipo 2",
            "custom_relevantes": ["Abc", "Def", "Ghi"],
            "custom_razonvisita": ["Lugar de descanso", "Mala ubicacion"],

            "lat": -33.5089381165112,
            "lng": -70.61913143268338,
        },

        {
            "name": "Ubicacion 3 - Prueba",
            "comuna": "Puente Alto",

            "tipo": "Lugar tipo 3",
            "custom_relevantes": ["Patrimonios Mas o menos", "Edificios bajos", "Biblioteca estandar"],
            "custom_razonvisita": ["Aire libre", "Razon 2"],

            "lat": -33.52089371165112,
            "lng": -70.62913133268338,
        },
    ]

    zones = []
    return render(request, "maps/v_puntosinteres.html", {"places": places, "zones": zones})

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