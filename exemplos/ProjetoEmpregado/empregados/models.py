from django.db import models

class Empregado(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50)
    data_contratacao = models.DateField()

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
