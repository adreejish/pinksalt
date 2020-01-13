from django.shortcuts import render
from django.http import HttpResponse
from pink_salt_app.models import Page

def index(request,pagename):
	pagename='/'+pagename
	pg=Page.objects.get(permalink=pagename)
	context={
		'title':pg.title,
		'content':pg.bodytext,
		'last_updated':pg.update_date,
		}
	#return HttpResponse("<h1> Homepage </h1>")
	#return render(request,'base.html')
	return render(request, 'pink_salt_app/pink_salt_app.html',context)
# Create your views here.
