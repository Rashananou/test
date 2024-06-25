from django.db import models


class car (models.Model):
	brand = models.CharField(max_length=50)
	color = models.CharField(max_length=50)
	price = models.IntegerField()

	def  __str__(self):
		return self.brand,self.color,self.price

