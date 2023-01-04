from django import forms
from .models import Pedidos

class FormPedido(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['status_de_pagamento']