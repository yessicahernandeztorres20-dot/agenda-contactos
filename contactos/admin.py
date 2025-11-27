from django.contrib import admin
from .models import Categoria, Contacto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'categoria']
    list_filter = ['categoria']