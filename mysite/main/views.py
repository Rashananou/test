from django.shortcuts import render
from django.http import HttpResponse
from .models import car

# Create your views here.

def index(response):
	return render(response,"main/base.html",{})

def index(response):
	return render(response,"main/home.html",{})

def gallery(request):
	savedcar = car.objects.all()
	context={'savedcar':savedcar}	
	return render(request,"main/gallery.html",context)


def addcar(request):
	if request.method=='POST' :
		brand=request.POST['brand']
		color=request.POST['color']
		price=request.POST['price']
		newcar= car(brand=brand , color=color,price=price)
		newcar.save()
	return render(request,"main/addcar.html",{})

def about(response):
	return render(response,"main/about.html",{})
