from django.db import models
from django.contrib.auth.models import User
import datetime
 
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=("user"), on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    banner = models.ImageField(default='fallback.png', blank=True, upload_to='uploads/')
    
class Service(models.Model):
    banner = models.ImageField(default='fallback.png', blank=True, upload_to='uploads/')
    service_name = models.CharField(max_length=100, null=True)
    provider_name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    advance_cost = models.DecimalField(max_digits=10, decimal_places=2)
    est_final_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.service_name} - {self.provider_name}"

class Portfolio(models.Model):
    name = models.CharField(max_length=100, default='Product')
    image = models.ImageField(default='fallback.png', blank=True, upload_to='uploads/')

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(default='fallback.png', blank=True, upload_to='uploads/')

class Review(models.Model):
    review = models.CharField(max_length=500)
    reviewer_name = models.CharField(max_length=100)
    reviewer_designation = models.CharField(max_length=100)
    reviewer_image = models.ImageField(default='fallback.png', blank=True, upload_to='uploads/')

class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)

class UserForm(models.Model):
    wed_date = models.DateField()
    city = models.CharField(max_length=100)
    services = models.CharField(max_length=500)
    event_mgr = models.CharField(max_length=10)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

class SpForm(models.Model):
    name = models.CharField(max_length=100)
    stype = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)