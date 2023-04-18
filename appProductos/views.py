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
def regProducto(request, idProd, msj = None):
    #consultar
    idProd = int(idProd)
    regProductos = Producto.objects.get(id= idProd)
    #ensamblar context
    context ={
            'producto' : regProducto,
            'titulo' : 'detalles de '+ str(regProducto.nombre),
    }
    if msj:
        context['mensaje']= msj
    #renderizar
    return render(request, 'productos/productos.html', context)
def agregarCarro(request, idProd):
    idProd = int(idProd) 
    regUsuario = request.user 
    msj = None
    #leer reg del producto en Producto
    existe = Producto.objects.filter(id=idProd).exists() 
    if existe:
        regProducto = Producto.objects.get(id=idProd)


        # si no existe en carrito:
        existe = Carro.objects.filter(producto=regProducto, estado= 'activo', usuario= regUsuario).exists()
if existe:
# instanciar un objeto de la clase Carrito
regCarro = Carro.objects.get(producto=regProducto, estado= 'activo', usuario= regUsuario) #incrementar cantidad
regCarro.cantidad += 1 
else:
regCarro = Carro(producto=regProducto, usuario= regUsuario, valUnit = regProducto.precioUnitario)

# guardar el registro regCarro.save()

else:
# dar mensaje
msj = 'Producto no disponible'


# redireccionar a 'verProducto' return verProducto(request, idProd, msj)

