from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    bio = models.TextField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='images/',default='default.png')
    location = models.CharField(max_length=50, blank=True,null=True)
    hood =models.ForeignKey('Neighborhood', on_delete=models.CASCADE,related_name='occupants',null=True,blank=True)
    
    def __str__(self):
        return f'{self.user.username}Profile'
    
class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500,blank=True)
    
    def __str__(self):
       return f'{self.name}Neighborhood'
   
    def save_hood(self):
        self.save()
        
    def delete_hood(self):
        self.delete()
        
    @classmethod
    def search_hoods(cls,name):
        return cls.objects.filter(name_icontains=name).all()
    








