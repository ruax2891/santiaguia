from django.shortcuts import render

def map_view(request):
    places = [
        {
            "name": "USM San Joaquin",
            "custom_type": "Universidad",

            "lat": -33.49089371165112,
            "lng": -70.61913133268338
        },
    ]
    return render(request, "maps/map.html", {"places": places})