from django.shortcuts import render, redirect
from .models import Courses

def index(request):
    context={
    "courses": courses.objects.all()
    }
    return render(request, "first_app/index.html", context)

def adding(request):
    courses.objects.create(title=request.POST['name'], description= request.POST['description'])
    return redirect('/')

def removing(request):
    context={
    'courses': courses.objects.name()
    }
    return render(request, "first_app/confirmation.html")
