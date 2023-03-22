from django.db import models

class register(models.Model):
	name=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)
	password=models.CharField(max_length=255)

class contact(models.Model):
	username=models.CharField(max_length=255)
	userphone=models.CharField(max_length=255)
	usermessage=models.CharField(max_length=255)
	useremail=models.CharField(max_length=255)

class service(models.Model):
	servicename=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	image=models.ImageField(upload_to='media/')

class gallery_tb(models.Model):
	image=models.ImageField(upload_to='media/')
	caption=models.CharField(max_length=255)

class getprice_tb(models.Model):
	sid=models.ForeignKey(service,on_delete=models.CASCADE)
	username=models.CharField(max_length=255)
	useremail=models.CharField(max_length=255)
	userphone=models.CharField(max_length=255)
	details=models.CharField(max_length=255)