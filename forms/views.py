from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

from .models import Pregunta, Respuesta
from .forms import RespuestaForm

def index(request):
    #preguntas = Pregunta.objects.order_by('id_numerico')
    form = RespuestaForm()
    template = loader.get_template("forms/index.html")
    contexto = {"form": form}
    if request.method == 'POST':
        if 'enviar' in request.POST:
            form = RespuestaForm(request.POST)
            form.save()
    return HttpResponse(template.render(contexto, request))

def respuestas(request):
    usuario = request.user
    if usuario.is_authenticated and usuario.has_perm('forms.view_respuesta'): # check si es usuario curador
        template = loader.get_template("forms/respuestas.html") # mandar context de respuestas y eso
        contexto = {"respuestas": Respuesta.objects.all()}
        return HttpResponse(template.render(contexto, request))
    else:
        raise PermissionDenied()
    