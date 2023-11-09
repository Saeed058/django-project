from django.db import models
from django.contrib.auth.models import User

class Object(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='cart/')

	def __str__(self):
		return self.name

class Kala(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='cart/')

	def __str__(self):
		return self.name

class CartItem(models.Model):
	object = models.ForeignKey(Object, on_delete=models.CASCADE)
	kala = models.ForeignKey(Kala, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.quantity} x {self.object.name} x {self.kala.name}'