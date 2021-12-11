from django.db import models

# Create your models here.


class Order(models.Model):
    # ordermodel
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    address_street = models.CharField(max_length=40)
    address_landmark = models.CharField(max_length=40)
    address_pincode = models.CharField(max_length=10)


class Product(models.Model):
    # product name model
    name = models.CharField(max_length=30)


class OrderItem(models.Model):
    # order place deatil model
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=40)
    prize = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
