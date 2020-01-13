from django.urls import path
import pink_salt_app.views

urlpatterns=[
#path('',pink_salt_app.views.index,name="index"),
path('',pink_salt_app.views.index,{'pagename':''},name='home'),
path('<str:pagename>',pink_salt_app.views.index,name='index'),
]
