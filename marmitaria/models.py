from django.db import models

# Create your models here.
class Prato(models.Model):
    MARMITA = "M"
    LANCHE = "L"
    ACOMPANHAMENTO = "A"
    SALGADO = "S"
    DOCE = "D"
    CATEGORIAS_PRATOS = {
        MARMITA: "Marmita",
        LANCHE: "Lanche",
        ACOMPANHAMENTO: "Acompanhamento",
        SALGADO: "Salgado",
        DOCE: "doce",
    }

    nome_prato = models.CharField(max_length=50)
    descricao = models.TextField()
    quant_calorias = models.IntegerField()
    img_prato = models.ImageField(upload_to="img_pratos/")