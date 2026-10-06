from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("mapa/", include("mapa.urls")),
    path("admin/", admin.site.urls)
]