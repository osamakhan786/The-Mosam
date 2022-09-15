from django.db import models

# Create your models here.
class Apipost(models.Model):
    name = models.CharField(max_length=250)
    address  = models.CharField(max_length=250)
    citt  = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name