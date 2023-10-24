from django.contrib.auth.models import User
from django.shortcuts import render
from .models import person
from .models import places
#Create your views here.

def inde(request):
    obj=places.objects.all()
    object=person.objects.all()
    return render(request, "index.html",{'result':obj,'res':object})


