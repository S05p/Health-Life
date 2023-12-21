from ckeditor.widgets import CKEditorWidget
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
    goods_introduction = forms.CharField(
        label_suffix='',label='',
        widget= CKEditorWidget(
            attrs={
                'style':'width:573.750px;height:439.464px'
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
        max_value=999999,min_value=0,
        widget = forms.NumberInput(
            attrs = {
                'class':'form-control',
                'placeholder':'가격'
            }
        )
    )
    class Meta:
        model = Goods
        fields = ('goods_name','goods_introduction','stock','price',)