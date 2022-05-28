from unicodedata import category
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=False,blank=False)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    location = models.CharField(max_length=100, null=False,blank=False)
    
    def __str__(self):
        return self.location
    
class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location,on_delete=models.SET_NULL, null=False, blank=False)
    image = models.ImageField(null=False,blank=False)
    description = models.TextField()
    
    def __str__(self):
        return self.description
    

