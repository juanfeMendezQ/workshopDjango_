from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.verCategorias, name='categorias'), 
    path('productos/<str:idCategoria>', views.verProductos, name='productos'),
]