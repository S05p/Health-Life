from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm
from .models import User
# Create your views here.


def join(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/join.html',context)

@login_required
def user_info(request,pk):
    user = get_object_or_404(User,pk=pk)
    context = {
        'user':user,
    }
    return render(request,'accounts/user_info.html',context)

@login_required
def update(request,pk):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context= {
        'form':form
    }
    return render(request,'accounts/update.html',context)

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect('articles:index')
    else:
        form =CustomAuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)