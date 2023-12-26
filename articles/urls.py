from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('detail/<int:article_pk>',views.detail,name='detail'),
    path('report/<int:article_pk>/',views.report_view,name='report_view'),
    path('detail/<int:article_pk>/likes/',views.article_like,name='article_like'),
    path('detail/<int:article_pk>/unlikes/',views.article_unlike,name='article_unlike'),
    path('category/<str:category_name>',views.category,name='category'),
    path('detail/<int:article_pk>/delete',views.delete,name='delete'),
    path('detail/<int:article_pk>/update',views.update,name='update'),
    path('category/<str:category_name>/search/',views.category_search,name='category_search'),
]
