from django.db import models # type: ignore

# Create your models here.
class Users(models.Model):
	_userName = models.CharField(max_length=100)
	_firstName = models.CharField(max_length=100)
	_lastName = models.CharField(max_length=100)
	_email = models.EmailField(max_length=100)
	_password = models.CharField(max_length=100)