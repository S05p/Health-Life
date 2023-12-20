from django import forms
from .models import *

class Goods_Form(forms.ModelForm):
    goods_name = forms.CharField(
        label_suffix='',label='',
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': '상품명'
            }
        )
    )
    stock = forms.IntegerField(
        label_suffix='',label='',
        widget = forms.NumberInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    price = forms.IntegerField(
        label_suffix='',label='',
        widget = forms.NumberInput(
            attrs = {
                'class':'form-control',
                'placeholder':'가격'
            }
        )
    )
    class Meta:
        models = Goods
        fields = ('goods_name','goods_introduction','stock','price',)