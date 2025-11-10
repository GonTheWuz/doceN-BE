from django.shortcuts import render
from .models import Person

def secunpart(request):
    return render (request, 'task2.html')

def person_detail(request, slug):
    person = Person.objects.get(slug=slug)
    return render(request, 'task5.html', {'person':person})