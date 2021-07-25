from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    Phone=models.CharField(max_length=10)
    message=models.TextField()

    def __str__(self):
        return self.name
    

class Payment(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    username=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    zip=models.IntegerField()
    payment=models.TextField()
    cardname=models.CharField(max_length=122)
    cardno=models.IntegerField()
    expiration=models.IntegerField()
    cvv=models.IntegerField()

    def __str__(self):
        return self.firstname+self.lastname
    
