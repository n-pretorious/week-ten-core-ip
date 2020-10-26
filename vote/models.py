from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
  photo = CloudinaryField('photo')
  name=models.CharField(max_length=20)
  userName=models.CharField(max_length=10, blank=True)
  contact=models.EmailField(max_length=254)
  bio=models.TextField()
  
  def __str__(self):
    return self.name
  
  class Meta:
      ordering = ['name']
      
  def saveProfile(self):
    self.save()
  