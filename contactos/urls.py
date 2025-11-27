from django.urls import path
from .views import ListaContactosView, DetalleContactoView, CrearContactoView, EditarContactoView, EliminarContactoView

urlpatterns = [
    path('', ListaContactosView.as_view(), name='lista_contactos'),
    path('detalle/<int:pk>/', DetalleContactoView.as_view(), name='detalle_contacto'),
    path('crear/', CrearContactoView.as_view(), name='crear_contacto'),
    path('editar/<int:pk>/', EditarContactoView.as_view(), name='editar_contacto'),
    path('eliminar/<int:pk>/', EliminarContactoView.as_view(), name='eliminar_contacto'),
]