from django.shortcuts import render
from girls.models import *
# Create your views here.

def index(request):
    category = CategoryGirls.objects.all()
    girls = Girls.objects.all().order_by('id')[:8]
    context = {
        'category':category,
        'girls':girls,
    }
    return render(request,'index.html',context)
    