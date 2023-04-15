from django.db import models
from produtos.models import Produtos
from django.contrib.auth.models import User

from django.db.models.signals import post_save


class Pedidos(models.Model):

    STATUS_PAGAMENTO = (
        ('pago', 'Pago'),
        ('pendente', 'Pendente'),
    )

    STATUS_PEDIDO_CHOICE = (
        ('pendente', 'Pendente'),
        ('preparando', 'Preparando'),
        ('pronto', 'Pronto')
    )

    usuario = models.CharField(max_length=150)
    pedidos = models.ManyToManyField(Produtos, blank=True, related_name="pedidos")
    numero_da_mesa = models.IntegerField(null=False, blank=True)
    nome_do_cliente = models.CharField(max_length=150)
    data_do_pedido = models.DateTimeField(auto_now_add=True)
    valor_da_compra = models.DecimalField(decimal_places=2, max_digits=10, default=0, blank=True)
    status_do_pedido = models.CharField(choices=STATUS_PEDIDO_CHOICE, max_length=15, blank=True, null=True)
    status_de_pagamento = models.CharField(choices=STATUS_PAGAMENTO, max_length=15, blank=True, null=True)
    

    def save(self, *args, **kwargs):
        if not self.status_de_pagamento and not self.status_do_pedido:
            self.status_de_pagamento = 'pendente'
            self.status_do_pedido = 'pendente'
        super().save(*args, **kwargs)

    

    def __str__(self):
        return str(self.numero_da_mesa) + ' --- ' + self.nome_do_cliente