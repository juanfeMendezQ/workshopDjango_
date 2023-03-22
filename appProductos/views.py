from django.shortcuts import render
from .models import *

# Create your views here.
def verCategorias(request):
    categorias = Categoria.objects.all()
    
    # ensamblar contexto
    context = {
        'categorias': categorias,
        'titulo': 'Categorias de productos del Supermercado',
    }
    # renderizar 
    return render(request, 'appProductos/categorias.html', context)
def verProductos(request, idCategoria):
    # consultar la categoria
    idCat = int(idCategoria)
    nombreCat = Categoria.objects.get(id=idCat)
    listaProductos = Producto.objects.filter(categoria=idCat)
    
    # ensamblar contexto
    context = {
        'productos': listaProductos,
        'titulo': 'Productos de la categoria: ' + str(nombreCat)
    }
    # renderizar 
    return render(request, 'productos/productos.html', context)
