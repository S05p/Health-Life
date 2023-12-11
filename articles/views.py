from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from datetime import datetime
from django.contrib import messages
# Create your views here.

def index(request):
    articles = Articles.objects.all().order_by('-pk')
    context = {
        'articles':articles,
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
            category = form.cleaned_data['category']
            category_instance = Category.objects.get(name=category)
            article = Articles.objects.create(
                User = request.user,
                title = title,
                content= content,
                upload_time = upload_time,
                category = category_instance
            )
            return redirect('articles:detail',article.pk)
    else:
        form = ArticlesForm()
    context = {
        'form': form,
    }
    return render(request,'articles/create.html',context)

def detail(request,article_pk):
    article = Articles.objects.get(pk=article_pk)
    comments = Comment.objects.filter(articles__id=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.User = request.user
            comment.articles = Articles.objects.get(pk=article_pk)
            comment.save()
            return redirect('articles:detail',article_pk)
    else:
        form = CommentForm()
    context = {
        'article': article,
        'form': form,
        'comments':comments,
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

def category(request,category_name):
    category_name = category_name.replace('-','')
    category = get_object_or_404(Category,name=category_name)
    articles = Articles.objects.filter(category=category)
    context = {
        'category':category,
        'articles':articles,
    }
    return render(request,'articles/category.html',context)
