from django.db import models

# Create your models here


class Registration(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50,unique=True)
    Email = models.EmailField(max_length=254,unique=True)
    Password = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
    
class Document(models.Model):
    pp=models.ImageField(upload_to='Profile_Photo')
    ac=models.ImageField( upload_to='Aadhar_Card')
    pc=models.ImageField( upload_to='Pan_Card' )
    vip=models.ImageField( upload_to='Voter_Id_Proof')
    ms=models.ImageField( upload_to='Marksheet')
    
