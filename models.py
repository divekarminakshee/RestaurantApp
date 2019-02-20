from django.db import models

# Create your models here.

class Customer(models.Model):
    STATUS_CHOICES = (
        ('higher class', 'Higher Class'),
        ('middle class', 'Middle Class'),
    )
    name= models.CharField(max_length=100)
 #   status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='middle class')
    address =  models.TextField()
    intime = models.DateTimeField(auto_now_add=True)
    outtime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
