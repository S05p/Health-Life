from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticlesForm
from .models import Articles
from datetime import datetime
from django.contrib import messages
# Create your views here.

def index(request):
    articles = Articles.objects.all().order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html',context)

@login_required
def create(request):
    if request.method == "POST":
        form = ArticlesForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            upload_time = datetime.now()
            article = Articles.objects.create(
                User = request.user,
                title = title,
                content= content,
                upload_time = upload_time,
            )
            return redirect('articles:detail',article.pk)
    else:
        form = ArticlesForm()
    context = {
        'form': form,
    }
    return render(request,'articles/create.html',context)

def detail(request,pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request,'articles/detail.html',context)

@login_required
def article_like(request,article_pk):
    article = get_object_or_404(Articles,pk=article_pk)
    if article.User == request.user:
        messages.error(request,'자신의 글은 추천 할 수 없습니다')
    if article.like_user.filter(pk=request.user.pk).exists() or article.unlike_user.filter(pk=request.user.pk).exists():
        return redirect('articles:detail',article_pk)
    else:
        article.like_user.add(request.user)
    return redirect('articles:detail', article_pk)

@login_required
def article_unlike(request,article_pk):
    article = get_object_or_404(Articles,pk=article_pk)
    if article.User == request.user:
        messages.error(request,'자신의 글은 비추천 할 수 없습니다.')
    if article.like_user.filter(pk=request.user.pk).exists() or article.unlike_user.filter(pk=request.user.pk).exists():
        return redirect('articles:detail', article_pk)
    else:
        article.unlike_user.add(request.user)
    return redirect('articles:detail',article_pk)
