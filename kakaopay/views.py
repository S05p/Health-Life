from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

# admin key = 398f8adf410adf67c806e42a4b92ccd6

@staff_member_required
def goods_registration(request):
    if request.method == 'POST':
        form = Goods_Form(request.POST,request.FILES)
        if form.is_valid():
            goods_name = form.cleaned_data['goods_name']
            goods_introduction = form.cleaned_data['goods_introduction']
            stock = form.cleaned_data['stock']
            price = form.cleaned_data['price']
            Goods.objects.create(
                goods_name = goods_name,
                goods_introduction = goods_introduction,
                stock = stock,
                price = price,
            )
            return redirect('kakaopay:goods_detail')
    else:
        form = Goods_Form()
    context = {
        'form':form,
    }
    return render(request,'kakaopay/goods_registration.html',context)

def goods_detail(request,goods_pk):
    goods = get_object_or_404(Goods,pk=goods_pk)
    context = {
        'goods':goods,
    }
    return render(request,'kakaopay/goods_detail.html',context)

@staff_member_required
def goods_update(request,goods_pk):
    goods = get_object_or_404(Goods,pk=goods_pk)
    if request.method == 'POST':
        form = Goods_Form(request.POST,request.FILES,instance=goods)
        if form.is_valid():
            goods_name = form.cleaned_data['goods_name']
            goods_introduction = form.cleaned_data['goods_introduction']
            stock = form.cleaned_data['stock']
            price = form.cleaned_data['price']
            goods.goods_name = goods_name
            goods.goods_introduction = goods_introduction
            goods.stock = stock
            goods.price = price
            goods.save()
            return redirect('kakaopay:detail')
    else:
        form = Goods_Form(instance=goods)
    context = {
        'goods_pk':goods_pk,
        'form':form,
    }
    return render(request,'kakaopay/goods_correction.html',context)


# goods_name = models.CharField(max_length=1000, null=False, blank=False)
# goods_introduction = RichTextUploadingField(blank=True, null=True)
# goods_code = models.PositiveIntegerField(primary_key=True, auto_created=True)
# stock = models.IntegerField()
# price = models.PositiveIntegerField()