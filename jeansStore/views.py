from django.http import HttpResponse
from django.shortcuts import render
from jeans.models import JeansStore

def home(request):
    jeans_store = JeansStore.objects.all()
    return render(request, 'home.html', {'jeans_store':jeans_store})