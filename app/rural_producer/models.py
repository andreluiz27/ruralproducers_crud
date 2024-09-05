from django.db import models

# Create your models here.

# Adding RuralProducer model
class RuralProducer(models.Model):

    # making models with this data
    # name = forms.CharField(max_length=100)
    # cpf = forms.CharField(max_length=11, label="CPF")

    # # related to the address
    # city = forms.CharField(max_length=100)
    # state = forms.CharField(max_length=2)

    # # related to the farm
    # farm_name = forms.CharField(max_length=100)
    # farm_area = forms.FloatField()
    # vegetation_area = forms.FloatField()

    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)
    crops = models.ManyToManyField('Crop')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return
