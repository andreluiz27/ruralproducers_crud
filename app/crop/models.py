from django.db import models

# Create your models here.


class Crop(models.Model):
    crop_plantation_types = [
        ("SOY", "Soy"),
        ("CORN", "Corn"),
        ("TOBACCO", "Tobacco"),
        ("RICE", "Rice"),
    ]
    crop_plantation = models.CharField(max_length=30, choices=crop_plantation_types, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # setting name in database as crop
    class Meta:
        verbose_name = "Crop"
        verbose_name_plural = "Crops"
        db_table = "crop"

    def __str__(self):
        return self.crop_plantation
