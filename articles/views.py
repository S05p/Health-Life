from django.shortcuts import render

# Create your views here.

def index(request):
    print('성공')
    return render(request,'articles/index.html')