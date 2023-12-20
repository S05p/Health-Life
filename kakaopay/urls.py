from django.urls import path
from . import views

app_name = 'kakaopay'
urlpatterns = [
    path('goods_registration',views.goods_registration,name='goods_registration'),
    path('goods_detail/<int:goods_pk>/',views.goods_detail,name='goods_detail'),

]
