from django.db import models

# Create your models here.
class Prato(models.Model):
    nome_prato = models.CharField(max_length=50)
    descricao = models.TextField()
    quant_calorias = models.IntegerField()
    img_prato = models.ImageField(upload_to="img_pratos/")

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)