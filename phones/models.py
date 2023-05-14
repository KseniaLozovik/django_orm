from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_digits=12, decimal_places=0, null=False)
    image = models.CharField(max_length=1000, null=False)
    release_date = models.CharField(max_length=50, null=False)
    lte_exists  = models.BooleanField(null=False)
    slug = models.SlugField(max_length=200, null=False)
    pass

