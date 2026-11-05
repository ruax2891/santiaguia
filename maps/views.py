from django.shortcuts import render

def mapa_puntos_interes(request):
    places = [
        {
            "name": "USM San Joaquin",

            "custom_type": "Universidad",
            "custom_relevantes": ["Patrimonios", "Edificios", "Biblioteca"],
            "custom_razonvisita": ["Lugar de estudios"],

            "lat": -33.49089371165112,
            "lng": -70.61913133268338,

        },
    ]
    return render(request, "maps/puntosinteres.html", {"places": places})

def mapa_riesgo_zonas(request):
    places = [
        {
            "name": "Not Usm",

            "custom_type": "Universidad",
            "custom_relevantes": ["Patrimonios", "Edificios", "Biblioteca"],
            "custom_razonvisita": ["Lugar de estudios"],

            "lat": -33.49089371165112,
            "lng": -70.61913133268338,

        },
    ]
    return render(request, "maps/puntosinteres.html", {"places": places})