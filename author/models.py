from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    # bio = models.TextField(null=True,blank=True)
    phone_no = models.CharField(max_length=12,null=True,blank=True)
    
    def __str__(self):
        return self.name