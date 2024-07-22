from django.db import models


# Create your models here.
class JimenezQuispeHubertJared(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.TextField()
    sexo = models.TextField()
    fecha_de_registro = models.TextField()




