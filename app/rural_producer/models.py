from django.db import models

# Create your models here.

# Adding RuralProducer model
class RuralProducer(models.Model):
    name = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=14, unique=True)
    farm = models.ForeignKey('farm.Farm', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
