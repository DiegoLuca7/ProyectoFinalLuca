from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def us(request):
    return render (request, "us.html", context={})