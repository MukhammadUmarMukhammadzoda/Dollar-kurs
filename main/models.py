from django.db import models

# Create your models here.

class Banklar(models.Model):
    nomi = models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.nomi

class Kurs(models.Model):
    bank = models.CharField(max_length=100, null=True,blank=True)
    dollar_olish = models.FloatField(max_length=20,null=True,blank=True)
    euro_olish = models.FloatField(max_length=20,null=True,blank=True)
    euro_sotish = models.FloatField(max_length=20,null=True,blank=True)
    dollar_sotish = models.FloatField(max_length=20,null=True,blank=True)
    
