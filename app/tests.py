from django.test import TestCase

# Create your tests here.

object 2 = Name
items style




@login_required
def buscarHistorias (request,):
    return render(request,"buscarHistorias.html")
@login_required
def encontrarHistorias (request,):
    if request.GET["buscarHistorias"]:
        patron = request.GET["buscarHistorias"]
        Historias = historias.objects.filter(nombre__icontains=patron)
        contexto = {"Historias": Historias}
        return render (request, "app/Historias_list.html", contexto)

    contexto = {"Historias": historias.objects.all()}
    return render (request, "app/Historias_list.html", contexto)

    path("buscarHistorias/",buscarHistorias, name="buscarHistorias"),
    path("encontrarHistorias/",encontrarHistorias, name="encontrarHistorias"),