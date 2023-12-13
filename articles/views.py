from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    articles = Articles.objects.filter(popular_article=True).order_by('-pk')
    page = int(request.GET.get('page',1))
    paginator = Paginator(articles,15)
    board = paginator.get_page(page)
    context = {
        'board':board,
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
    comments = Comment.objects.filter(articles__id=article_pk,parent_comment=None)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data['content']
                parent_comment_id = form.cleaned_data['parent_comment_id']
                if parent_comment_id:
                    parent_comment = get_object_or_404(Comment,pk=parent_comment_id)
                    Comment.objects.create(User=request.user,articles=article,content=content,parent_comment=parent_comment)
                else:
                    Comment.objects.create(User=request.user, articles=article, content=content)
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
        if article.like_user.count() >= 10 and article.like_user.count() >= article.unlike_user.count():
            article.popular_article = True
            article.save()
    return redirect('articles:detail',article_pk)

@login_required
def article_unlike(request,article_pk):
    article = get_object_or_404(Articles,pk=article_pk)
    if article.User == request.user:
        messages.error(request,'자신의 글은 비추천 할 수 없습니다.')
    if article.like_user.filter(pk=request.user.pk).exists() or article.unlike_user.filter(pk=request.user.pk).exists():
        return redirect('articles:detail', article_pk)
    else:
        article.unlike_user.add(request.user)
    if article.popular_article == True and article.like_user.count() <= article.unlike_user.count():
        article.popular_article = False
    return redirect('articles:detail',article_pk)

def category(request,category_name):
    category_name = category_name.replace('-','')
    category = get_object_or_404(Category,name=category_name)
    articles = Articles.objects.filter(category=category).order_by('-pk')
    page = int(request.GET.get('page', 1))
    paginator = Paginator(articles, 10)
    board = paginator.get_page(page)
    context = {
        'category':category,
        'board':board,
    }
    return render(request,'articles/category.html',context)
