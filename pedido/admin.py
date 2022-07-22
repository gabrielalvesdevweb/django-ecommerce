from django.contrib import admin
from . import models

class ItemPedidoInline(admin.TabularInline):
    model = models.ItemPedido
    estra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]

admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.ItemPedido)