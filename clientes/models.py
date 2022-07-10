from django.db import models


# Create your models here.
class Clientes(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    rg = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.nome} | {self.email}"
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

