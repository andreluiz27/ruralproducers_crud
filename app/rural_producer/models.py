from django.db import models

# Create your models here.

# Adding RuralProducer model
class RuralProducer(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    farm = models.ForeignKey('farm.Farm', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return
