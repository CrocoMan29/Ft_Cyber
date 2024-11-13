from django.db import models # type: ignore

# Create your models here.
class Users(models.Model):
	username = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)