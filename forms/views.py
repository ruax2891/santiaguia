from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Pregunta, Respuesta
from .forms import RespuestaForm

def index(request):
    preguntas = Pregunta.objects.order_by('id_numerico')
    form = RespuestaForm()
    template = loader.get_template("forms/index.html")
    contexto = {"form": form}
    if request.method == 'POST':
        if 'guardar' in "request.POST":
            form = RespuestaForm(request.POST)
            form.save()
    return HttpResponse(template.render(contexto, request))

def respuestas(request):
    template = loader.get_template("forms/respuestas.html")
    contexto = {"respuestas": Respuesta.objects.all()}
    return HttpResponse(template.render(contexto, request))