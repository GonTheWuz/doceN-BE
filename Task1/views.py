from django.shortcuts import render

from task2.models import Person

def pagprinci(request):
    person_list = Person.objects.all()
    return render(request, 'inicio.html', {'persons': person_list})
