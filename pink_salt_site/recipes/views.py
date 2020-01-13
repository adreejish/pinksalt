from django.shortcuts import render
from django.http import HttpResponseRedirect

from recipes.models import Recipe
from recipes.forms import RecipeForm
from pink_salt_app.models import Page

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url=reverse_lazy('login'))
def recipe_req(request):
	submitted=False
	if request.method=='POST':
		form=RecipeForm(request.POST,request.FILES)
		if form.is_valid():
			inst=form.save(commit=False)
			try:
				inst.user=request.user
			except Exception:
				pass
			inst.save()
			#compress.showurl(inst.coverimage.url)
			#print (inst.coverimage)
			return HttpResponseRedirect('/recipe/?submitted=True')
	else:
		form=RecipeForm()
		if 'submitted' in request.GET:
			submitted=True
	return render(request,'recipes/submitrecipe.html',{'form':form,'submitted':submitted})	

class RecipeList(ListView):
	model=Recipe
	context_object_name='all_recipes'

class RecipeDetail(DetailView):
	model=Recipe
	context_object_name='recipe'	

class Register(CreateView):
	template_name='registration/register.html'
	form_class = UserCreationForm
	success_url=reverse_lazy('register-success')

	def form_valid(self,form):
		form.save()
		return HttpResponseRedirect(self.success_url)
