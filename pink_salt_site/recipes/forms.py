from django import forms
from django.forms import ModelForm
from recipes.models import Recipe

class RecipeForm(ModelForm):
	required_css_class='required'
	class Meta:
		model=Recipe
		fields=['title','time','serves','ingredients','directions','category','coverimage']
		
