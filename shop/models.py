from django.db import models
from django.core.validators import MinLengthValidator 
from django import forms 

 
def max_length_10(value):
         if len(value) > 10:
             raise forms.ValidationError('10글자 이상 !!!')

#max_length_10 = MaxLengthValidator(10) 
 


class Item(models.Model):
     name = models.CharField(max_length=100) 
     desc = models.TextField(blank=True) 
     price = models.PositiveIntegerField() 
     is_publish = models.BooleanField(default=False)
     created_at = models.DateTimeField(auto_now_add=True) 
     updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name