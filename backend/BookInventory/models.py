from django.db import models
from django.contrib.auth.models import User

class Inventory(models.Model):
    entry_id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=255)  
    author = models.CharField(max_length=255) 
    genre = models.CharField(max_length=100)  
    publication_date = models.DateField()  
    isbn = models.CharField(max_length=13, unique=True) 

    def __str__(self):
        return self.title
