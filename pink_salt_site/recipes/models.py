from django.db import models

# Create your models here.
from django.contrib.auth.models import User 

CATEGORY=(
	('A','Appetizer'),
	('E','Entree'),
	('S','Sides'),
	('M','Main Course'),
	('D', 'Dessert'),
	('B','Beverage'),
	('O','Other'),
)


class Recipe(models.Model):
	title=models.CharField(max_length=100)
	date=models.DateField(auto_now_add=True)
	time=models.DurationField('Cooking Time')
	serves=models.BigIntegerField('Serves')
	ingredients=models.TextField('Ingredients')
	directions=models.TextField('Cooking Directions')
	category=models.CharField(max_length=40,choices=CATEGORY)
	coverimage=models.ImageField(upload_to='coverimages/')
	user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.id)
	

