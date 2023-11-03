from django.db import models


# Create your models here.
class Employee(models.Model):
    FirstName = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField()
    Age = models.IntegerField(default=0)
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.FirstName+' '+self.Lastname


class Product(models.Model):
    ProductID = models.IntegerField(default=0)
    ProductName = models.CharField(max_length=50)
    ProductPrice = models.IntegerField(default=0)
    Description = models.CharField(max_length=300)

    def __str__(self):
        return self.ProductName