from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Create(models.Model):
	name = models.CharField(max_length=100)
	made_in = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='cart/')

	def __str__(self):
		return self.name 
	
class CreateItem(models.Model):
	create = models.ForeignKey(Create, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.quantity} x {self.create.name}'