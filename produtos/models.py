from django.db import models


class Categoria(models.Model):
    nome_da_categoria = models.CharField(max_length=150, verbose_name='Nome da categoria')

    def __str__(self):
        return self.nome_da_categoria
    


class Produtos(models.Model):
    nome_do_produto = models.CharField(max_length=150, blank=False, null=False)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.CASCADE)
    valor_do_produto = models.DecimalField(decimal_places=2, blank=False, null=False, max_digits=6)
    photo_do_produto = models.ImageField(upload_to='Image/')
    descricao_do_produto = models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.nome_do_produto 