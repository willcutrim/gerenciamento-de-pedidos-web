from django import forms
from .models import Produtos

class ProdutoForm(forms.ModelForm):
    
    class Meta:
        model = Produtos
        fields = "__all__"