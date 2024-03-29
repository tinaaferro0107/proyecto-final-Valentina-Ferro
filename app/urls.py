from django.urls import path, include
from app.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", home, name= "inicio"),
    path("acerca", acerca, name= "acerca"),
  

# personajes
    path("personajes/", personajeslist.as_view(), name= "personajes"),
    path("personajesCreate/", personajescreate.as_view(), name= "personajesCreate"),
    path("personajesUpdate/<int:pk>", personajesupdate.as_view(), name= "personajesUpdate"),
    path("personajesDelete/<int:pk>", personajesdelete.as_view(), name= "personajesDelete"),
    path("buscarPersonajes/",buscarPersonajes, name="buscarPersonajes"),
    path("encontrarPersonajes/",encontrarPersonajes, name="encontrarPersonajes"),
# mundos
    path("mundos/", mundoslist.as_view(), name= "mundos"),
    path("mundosCreate/", mundoscreate.as_view(), name= "mundosCreate"),
    path("mundosUpdate/<int:pk>", mundosupdate.as_view(), name= "mundosUpdate"),
    path("mundosDelete/<int:pk>", mundosdelete.as_view(), name= "mundosDelete"), 
    path("buscarMundos/",buscarMundos, name="buscarMundos"),
    path("encontrarMundos/",encontrarMundos, name="encontrarMundos"),
# objetos_magicos
    path("objetos_magicos/", objetos_magicoslist.as_view(), name= "objetos_magicos"),
    path("objetos_magicosCreate/", objetos_magicoscreate.as_view(), name= "objetos_magicosCreate"),
    path("objetos_magicosUpdate/<int:pk>", objetos_magicosupdate.as_view(), name= "objetos_magicosUpdate"),
    path("objetos_magicosDelete/<int:pk>", objetos_magicosdelete.as_view(), name= "objetos_magicosDelete"),
    path("buscarObjetos_magicos/",buscarObjetos_magicos, name="buscarObjetos_magicos"),
    path("encontrarObjetos_magicos/",encontrarObjetos_magicos, name="encontrarObjetos_magicos"),  
# historias
    path("historias/", historiaslist.as_view(), name= "historias"),
    path("historiasCreate/", historiascreate.as_view(), name= "historiasCreate"),
    path("historiasUpdate/<int:pk>", historiasupdate.as_view(), name= "historiasUpdate"),
    path("historiasDelete/<int:pk>", historiasdelete.as_view(), name= "historiasDelete"),
    path("buscarHistorias/",buscarHistorias, name="buscarHistorias"),
    path("encontrarHistorias/",encontrarHistorias, name="encontrarHistorias"),
    
#____________________ Login, Logout, Registration
    path('login/', login_request, name="login"),
    path('Logout/', Logout , name="Logout"),
    path('logout/', LogoutView.as_view(template_name="logout.html") , name="logout"),
    path('registrar/', register, name="registrar"),

#____________________ Edicion Perfil, Cambio de Clave, Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),



]