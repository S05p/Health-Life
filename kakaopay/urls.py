from django.urls import path
from . import views

app_name = 'kakaopay'
urlpatterns = [
    path('goods_registration/',views.goods_registration,name='goods_registration'),
    path('goods_detail/<int:goods_pk>/',views.goods_detail,name='goods_detail'),
    path('goods_detail/<int:goods_pk>/update/',views.goods_update,name='goods_update'),
    path('goods_detail/<int:goods_pk>/delete/',views.goods_delete,name='goods_delete'),
    paht('goods_detail/<int:goods_pk>/logic/',views.logic,name='logic'),
]
