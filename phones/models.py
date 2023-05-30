from django.db import models


class Phone(models.Model):

    name =  models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='phones/phone_images')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100)
