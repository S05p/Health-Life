from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm, CustomPasswordChangeForm
from .models import *
from django.contrib import messages
# Create your views here.


def join(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            hobby1 = form.cleaned_data['hobby1']
            hobby2 = form.cleaned_data['hobby2']
            hobby3 = form.cleaned_data['hobby3']
            hobby1 = Hobby.objects.get(name=hobby1)
            hobby2 = Hobby.objects.get(name=hobby2)
            hobby3 = Hobby.objects.get(name=hobby3)
            user = form.save()
            user.hobbies.add(hobby1,hobby2,hobby3)
            user.save()
            auth_login(request,user,backend='django.contrib.auth.backends.ModelBackend')
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
    hobbies_of_user0 = user.hobbies.all()[0]
    hobbies_of_user1 = user.hobbies.all()[1]
    hobbies_of_user2 = user.hobbies.all()[2]
    context = {
        'user': user,
        'hobbies_of_user0': hobbies_of_user0,
        'hobbies_of_user1': hobbies_of_user1,
        'hobbies_of_user2': hobbies_of_user2,
    }
    if request.user == user:
        return render(request, 'accounts/user_info.html', context)
    else:
        return redirect('articles:index')

@login_required
def update(request,pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST' and request.user == user:
        form = CustomUserChangeForm(request.POST,request.FILES,instance=request.user)
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
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request,request.POST)
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

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@login_required()
def password_change(request,pk):
    user = User.objects.get(pk=pk)
    if request.user != user:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,'비밀번호 변경에 성공했습니다.')
            update_session_auth_hash(request,user)
            return redirect('articles:index')
        else:
            messages.error(request,'변경하실 비밀번호를 확인해주세요')
    else:
        form = CustomPasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request,'accounts/password_change.html',context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

