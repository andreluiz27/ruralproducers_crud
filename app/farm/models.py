from django.db import models

# Create your models here.

class Farm(models.Model):
    farm_name = models.CharField(max_length=100)
    farm_area = models.FloatField()
    vegetation_area = models.FloatField()
    crops = models.ManyToManyField('crop.Crop')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Farm"
        verbose_name_plural = "Farms"
        db_table = "farm"

    def __str__(self):
        return self.farm_name
