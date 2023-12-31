from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Q

# Create your views here.

Goods = apps.get_model(settings.GOODS_MODEL)

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
            category = form.cleaned_data["category"]
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
def delete(request,article_pk):
    article = get_object_or_404(Articles,pk=article_pk)
    if request.user == article.User:
        article.delete()
        return redirect('articles:index')

@login_required
def update(request,article_pk):
    article = get_object_or_404(Articles,pk=article_pk)
    if request.method == 'POST':
        form = ArticlesForm(request.POST,request.FILES,instance=article)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            revise_time = datetime.now()
            category = form.cleaned_data["category"]
            category_instance = Category.objects.get(name=category)
            article.title = title
            article.content = content
            article.revise_time = revise_time
            article.category = category_instance
            article.save()
            return redirect('articles:detail',article_pk)
    else:
        form = ArticlesForm(instance=article)
    context = {
        'form':form,
        'article_pk':article_pk,
    }
    return render(request,'articles/update.html',context)
@login_required
def article_like(request,article_pk):
    article = get_object_or_404(Articles,pk=article_pk)
    if article.User == request.user:
        messages.error(request,'자신의 글은 추천 할 수 없습니다')
        return redirect('articles:detail', article_pk)
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
        return redirect('articles:detail', article_pk)
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
    if category_name == '팝업스토어':
        goods = Goods.objects.all().order_by('-pk')
        page = int(request.GET.get('page', 1))
        paginator = Paginator(goods, 10)
        board = paginator.get_page(page)
    else:
        articles = Articles.objects.filter(category=category).order_by('-pk')
        page = int(request.GET.get('page', 1))
        paginator = Paginator(articles, 10)
        board = paginator.get_page(page)
    context = {
        'category':category,
        'board':board,
        'category_name':category_name,
    }
    return render(request,'articles/category.html',context)

@login_required
def report_view(request,article_pk):
    if Report.objects.filter(report_article_pk=article_pk, User=request.user).exists():
        messages.error(request, '이미 신고한 글입니다.')
        return redirect('articles:detail', article_pk)
    if request.user == Articles.objects.get(pk=article_pk).User:
        messages.error(request, '자신의 글은 신고할 수 없습니다')
        return redirect('articles:detail',article_pk)
    if request.method == 'POST':
        form = ReportForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            reason = form.cleaned_data['reason']
            article = get_object_or_404(Articles,pk=article_pk)
            report_title = article.title
            report_content = article.content
            report_user_nickname = article.User.nickname
            report_article_pk = article_pk
            Report.objects.create(
                User = request.user,
                title = title,
                report_content = report_content,
                report_user_nickname = report_user_nickname,
                report_title = report_title,
                reason = reason,
                upload_time = datetime.now(),
                report_article_pk = report_article_pk,
            )
            messages.success(request, '신고가 성공적으로 제출되었습니다.')
            return redirect('articles:detail',article_pk)
    else:
        form = ReportForm()
    context = {
        'form':form,
        'article_pk':article_pk,
    }
    return render(request,'articles/report.html',context)

def category_search(request,category_name):
    if request.method == 'POST':
        category_name = category_name
        searched = request.POST['searched']
        select = request.POST.get('select',1)
        if category_name == '팝업스토어':
            if select == 1:
                articles = Goods.objects.filter(
                    Q(goods_name__contains=searched)|
                    Q(goods_introducion__contains=searched)
                ).order_by('-pk')
            elif select == 2:
                articles = Goods.objects.filter(
                    Q(goods_name__contains=searched)
                ).order_by('-pk')
            else:
                articles = Goods.objects.filter(
                    Q(goods_introduction__contains=searched)
                ).order_by('-pk')
        else:
            category_name = Category.objects.get(name=category_name)
            if select == 1:
                articles = Articles.objects.filter(
                    Q(title__contains=searched)|
                    Q(content__contains=searched),
                    Q(category=category_name)
                ).order_by('-pk')
            elif select == 2:
                articles = Articles.objects.filter(
                    Q(title__contains=searched) ,
                    Q(category=category_name)
                ).order_by('-pk')
            elif select == 3:
                articles = Articles.objects.filter(
                    Q(content__contains=searched) ,
                    Q(category=category_name)
                ).order_by('-pk')
            else:
                articles = Articles.objects.filter(
                    Q(User__nickname__contains=searched) ,
                    Q(category=category_name)
                ).order_by('-pk')
        return render(request,'articles/search.html',{'articles':articles,'category_name':category_name})
    else:
        return render(request,'articles/search.html')

