from django.urls import path
from . import views

app_name = "produto" # produto:lista

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name="lista"),
    path('<slug>', views.DetalheProduto.as_view(), name="detalhe"),
    path('addToCart/', views.AddToCart.as_view(), name="addtocart"),
    path('removeCart/', views.RemoveCart.as_view(), name="removecart"),
    path('cart/', views.Cart.as_view(), name="cart"),
    path('resumodacompra/', views.ResumoDaCompra.as_view(), name="resumodacompra"),
    path('busca/', views.Busca.as_view(), name="busca"),
]