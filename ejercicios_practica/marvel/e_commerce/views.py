from typing import Any
from django.shortcuts import render

# Importamos vistas genericas:
from django.views.generic import TemplateView

# Importamos los modelos que vamos a usar:
from django.contrib.auth.models import User
from e_commerce.models import *

class PruebaView(TemplateView):
    template_name = 'e-commerce/base_tp.html'

class Tarea_1_View(TemplateView):
    template_name = 'e-commerce/template_tarea.html'

class Tarea_2_View(TemplateView):
    template_name = 'e-commerce/template_tarea_2.html'

class CompraExitosa(TemplateView):
    template_name = 'e-commerce/gracias.html'

class LoginDeMiApp(TemplateView):
    template_name = 'e-commerce/login.html'

class UsuarioDatos(TemplateView):
    template_name = 'e-commerce/user.html'

class Carrito(TemplateView):
    template_name = 'e-commerce/cart.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        username = self.request.user
        user_obj = User.objects.get(username=username)
        wish_obj = WishList.objects.filter(user = user_obj, cart = True)
        comics_carrito = [obj.comic for obj in wish_obj]
        
        context['comics_carrito'] = comics_carrito
        
        return context
    
class Favoritos(TemplateView):
    template_name = 'e-commerce/wish.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        username = self.request.user
        user_obj = User.objects.get(username=username)
        wish_obj = WishList.objects.filter(user=user_obj, favorite=True)
        comics_favoritos = [obj.comic for obj in wish_obj]
        
        context['favoritos'] = comics_favoritos

        return context
