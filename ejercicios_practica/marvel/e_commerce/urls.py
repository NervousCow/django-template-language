from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.views import *


urlpatterns = [
    # NOTE: e_commerce base:
    path('base_tp', PruebaView.as_view(), name='base'),
    path('tarea_1', Tarea_1_View.as_view(), name='tarea1'),
    path('tarea_2', Tarea_2_View.as_view(), name='tarea2'),
    path('compra_exitosa', CompraExitosa.as_view(), name='compra-exitosa'),
    # Falta hacer makamigrations???
    path('login', LoginDeMiApp.as_view(), name='login-de-mi-app'),
    path('user', UsuarioDatos.as_view(), name='datos-de-usuario'),
    path('carrito', Carrito.as_view(), name='carrito'),
    path('favoritos', Favoritos.as_view(), name='favoritos'),

    #TODO: Tarea! 
    ]