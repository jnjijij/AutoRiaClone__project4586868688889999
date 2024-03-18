# backend/web-services/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'web-services/index.html')
