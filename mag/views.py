from django.http import HttpResponse
from django.shortcuts import render
from .models import Designation, Engin
import datetime

# Create your views here.
def index(request):
    desi = Designation.objects.all()
    eng = Engin.objects.all()
    
    return render(request, "mag/index.html", {
        "desi": desi,
        "engins": eng
    })
