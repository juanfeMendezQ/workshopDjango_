from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.verCategorias, name='categorias'), 
    path('productos/<str:idCategoria>', views.verProductos, name='productos'),
    path('producto/<str:idProd>',views.verProductos, name='un_procducto'),
    path('carro/<str:idProd>', views.agregarCarro, name='agregarCarro'), 
    path('carrito/', views.verCarrito, name='carrito'),
    path('eliminar/<str:id>', views.eliminarCarrito, name='eliminar'),
    path('cambiarCantidad/', views.cambiarCantidad),
]