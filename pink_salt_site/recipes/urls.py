from django.urls import path
from recipes import views
from recipes.views import RecipeList,RecipeDetail

urlpatterns=[
	path('',views.recipe_req,name='recipe-request'),
	path('browse/<int:pk>',RecipeDetail.as_view(),name='recipe-detail'),
	path('browse',RecipeList.as_view(),name='show-recipes'),]
