from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student

# Create your views here.
def index(requests):
    return render(requests, 'students/index.html',{
        'students': Student.objects.all()
    })
    
def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))    