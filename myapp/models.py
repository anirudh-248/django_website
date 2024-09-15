from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    banner = models.ImageField(default='fallback.png', blank=True)

class Service(models.Model):
    banner = models.ImageField(default='fallback.png', blank=True)
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

class Portfolio(models.Model):
    name = models.CharField(max_length=100, default='Product')
    image = models.ImageField(default='fallback.png', blank=True)

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(default='fallback.png', blank=True)

class Review(models.Model):
    review = models.CharField(max_length=500)
    reviewer_name = models.CharField(max_length=100)
    reviewer_designation = models.CharField(max_length=100)
    reviewer_image = models.ImageField(default='fallback.png', blank=True)