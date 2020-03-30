from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone=models.PositiveIntegerField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    picture=models.ImageField(upload_to="profile",default="none.jpg",blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.username

class Contacts(models.Model):
    firstname=models.CharField(max_length=20) 
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    address=models.TextField()
    def __str__(self):
        return self.firstname +" " + self.lastname


type = [
    ('footwear', 'footwear'),
    ('clothes','clothes'),
    ('jwellary', 'jwellary'),   
    ('handbags','handbags'),
    ('sportswear','sportswear')
]



class Product(models.Model):
    name=models.CharField(max_length=20)
    image= models.ImageField(upload_to="products", default="none.jpg", blank=True, null=True)
    type = models.CharField(max_length=10, choices=type)
    price=models.DecimalField(decimal_places=2,max_digits=20)
    rating=models.IntegerField()
    detail=models.TextField()

    def __str__(self):
        return self.name + " " + self.type

class Cart(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
