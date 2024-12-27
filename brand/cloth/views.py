from django.shortcuts import render


# Create your views here.
def home(re):
    return render(re, 'index.html')
