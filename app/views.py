from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


def home(request,):
    return render (request,"index.html")
@login_required
def acerca(request,):
    return render (request,"acercademi.html")



# personajes
class personajeslist(LoginRequiredMixin,ListView):
    model = personajes
@method_decorator(staff_member_required, name="dispatch")    
class personajescreate(LoginRequiredMixin,CreateView):
    model = personajes
    fields = ["nombre","especie","habilidades","imagen"]
    success_url = reverse_lazy("personajes")
@method_decorator(staff_member_required, name="dispatch")    
class personajesupdate(LoginRequiredMixin,UpdateView):
    model = personajes
    fields = ["nombre","especie","habilidades","imagen"]
    success_url = reverse_lazy("personajes")
@method_decorator(staff_member_required, name="dispatch")    
class personajesdelete(LoginRequiredMixin,DeleteView):
    model = personajes
    success_url = reverse_lazy("personajes")
@login_required
def buscarPersonajes (request,):
    return render(request,"buscarPersonajes.html")
def encontrarPersonajes (request,):
        if request.GET["buscarPersonajes"]:
            patron = request.GET["buscarPersonajes"]
            Personajes = personajes.objects.filter(nombre__icontains= patron)
            contexto = {"Personajes": Personajes}
            return render (request, "app/personajes_list.html", contexto)

        contexto = {"Personajes": personajes.objects.all()}
        return render (request, "app/personajes_list.html", contexto)


# mundos
class mundoslist(LoginRequiredMixin,ListView):
    model = mundos
@method_decorator(staff_member_required, name="dispatch")    
class mundoscreate(LoginRequiredMixin,CreateView,):
    model = mundos
    fields = ["nombre","habitantes","descripcion","imagen"]
    
    success_url = reverse_lazy("mundos")
@method_decorator(staff_member_required, name="dispatch")    
class mundosupdate(LoginRequiredMixin,UpdateView):
    
    model = mundos
    fields = ["nombre","habitantes","descripcion","imagen"]
    success_url = reverse_lazy("mundos")
@method_decorator(staff_member_required, name="dispatch")    
class mundosdelete(LoginRequiredMixin,DeleteView):
    model = mundos
    success_url = reverse_lazy("mundos")        
@login_required
def buscarMundos (request,):
    return render(request,"buscarMundos.html")
@login_required
def encontrarMundos (request,):
    if request.GET["buscarMundos"]:
        patron = request.GET["buscarMundos"]
        Mundos = mundos.objects.filter(nombre__icontains=patron)
        contexto = {"Mundos": Mundos}
        return render (request, "app/mundos_list.html", contexto)

    contexto = {"Mundos": mundos.objects.all()}
    return render (request, "app/Mundos_list.html", contexto)
    
# objetos_magicos
class objetos_magicoslist(LoginRequiredMixin,ListView):
    model = objetos_magicos
@method_decorator(staff_member_required, name="dispatch")    
class objetos_magicoscreate(LoginRequiredMixin,CreateView):
    model = objetos_magicos
    fields = ["nombre","descripción","dueño"]
    success_url = reverse_lazy("objetos_magicos")
@method_decorator(staff_member_required, name="dispatch")    
class objetos_magicosupdate(LoginRequiredMixin,UpdateView):
    model = objetos_magicos
    fields = ["nombre","descripción","dueño"]
    success_url = reverse_lazy("objetos_magicos")
@method_decorator(staff_member_required, name="dispatch")    
class objetos_magicosdelete(LoginRequiredMixin,DeleteView):
    model = objetos_magicos
    success_url = reverse_lazy("objetos_magicos")                
@login_required
def buscarObjetos_magicos (request,):
    return render(request,"buscarObjetos_magicos.html")
@login_required
def encontrarObjetos_magicos (request,):
    if request.GET["buscarObjetos_magicos"]:
        patron = request.GET["buscarObjetos_magicos"]
        Objetos_magicos = objetos_magicos.objects.filter(nombre__icontains=patron)
        contexto = {"Objetos_magicos": Objetos_magicos}
        return render (request, "app/Objetos_magicos_list.html", contexto)

    contexto = {"Objetos_magicos": objetos_magicos.objects.all()}
    return render (request, "app/Objetos_magicos_list.html", contexto)

# historias
class historiaslist(LoginRequiredMixin,ListView):
    model = historias
@method_decorator(staff_member_required, name="dispatch")    
class historiascreate(LoginRequiredMixin,CreateView):
    model = historias
    fields = ["nombre","resumen","protagonistas"]
    success_url = reverse_lazy("historias")
@method_decorator(staff_member_required, name="dispatch")    
class historiasupdate(LoginRequiredMixin,UpdateView):
    model = historias
    fields = ["nombre","resumen","protagonistas"]
    success_url = reverse_lazy("historias")
@method_decorator(staff_member_required, name="dispatch")    
class historiasdelete(LoginRequiredMixin,DeleteView):
    model = historias
    success_url = reverse_lazy("historias") 
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

#____________________ Login, Logout, Registration
def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            
            return render(request, "index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AuthenticationForm()

    return render(request, "login.html", {"form": miForm} )
def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('inicio'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = RegistroForm()

    return render(request, "registro.html", {"form": miForm} )  
def Logout (request):
    return render (request,"Log.html")

#____________________ Edicion Perfil, Cambio de Clave, Avatar
@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('inicio'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = UserEditForm(instance=usuario)

    return render(request, "editarPerfil.html", {"form": miForm} )      
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "cambiar_clave.html"
    success_url = reverse_lazy("inicio")
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar = Avatar(user=usuario, imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('inicio'))
    else:
        miForm = AvatarForm()

    return render(request, "agregarAvatar.html", {"form": miForm} )   