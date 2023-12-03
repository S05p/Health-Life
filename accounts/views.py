from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
# Create your views here.

def join(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request,request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/join.html',context)