from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contacto

class ListaContactosView(ListView):
    model = Contacto
    template_name = 'contactos/lista.html'
    context_object_name = 'contactos'

class DetalleContactoView(DetailView):
    model = Contacto
    template_name = 'contactos/detalle.html'
    context_object_name = 'contacto'

class CrearContactoView(CreateView):
    model = Contacto
    fields = ['nombre', 'telefono', 'email', 'categoria']
    template_name = 'contactos/crear.html'
    success_url = reverse_lazy('lista_contactos')

class EditarContactoView(UpdateView):
    model = Contacto
    fields = ['nombre', 'telefono', 'email', 'categoria']
    template_name = 'contactos/editar.html'
    success_url = reverse_lazy('lista_contactos')

class EliminarContactoView(DeleteView):
    model = Contacto
    template_name = 'contactos/eliminar.html'
    success_url = reverse_lazy('lista_contactos')