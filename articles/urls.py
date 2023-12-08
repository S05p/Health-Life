from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('detail/<int:article_pk>/likes/',views.article_like,name='article_like'),
    path('detail/<int:article_pk>/unlikes/',views.article_unlike,name='article_unlike'),
    path('category/<str:category_name>',views.category,name='category'),
]
