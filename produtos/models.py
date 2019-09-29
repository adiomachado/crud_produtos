from django.db import models

#criando a classe Produto com 3 atributos
class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.descricao