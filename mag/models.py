from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
import datetime

class Engin(models.Model):   
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=16)
    
    def __str__(self):
        return f"{self.name} {self.code}"

class Designation(models.Model):
    desi_name = models.CharField(max_length=32)
    eng_name = models.ForeignKey(Engin, on_delete=models.CASCADE, related_name="to_eng")
    desi_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.desi_name} {self.eng_name}"
    

