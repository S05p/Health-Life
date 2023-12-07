from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
from django.forms import ClearableFileInput
from .models import Articles, Comment

class ArticlesForm(forms.Form):
    Category_Choices = [
        ('big three exercises ', '3대운동'),
        ('Lean Mass Up', '린매스업'),
        ('cardio', '유산'),
        ('bodybilding', '보디빌딩'),
        ('diet', '식단'),
        ('freedom', '자유'),
    ]
    title = forms.CharField(
        label_suffix='',label='',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    image = forms.ImageField(
        label_suffix='',label='',
        required=False,
        widget=ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    content = forms.ChoiceField(
        label_suffix='',label='',
        widget=CKEditorWidget(
            attrs={
                'class':'form-control',
            }
        )
    )
    category = forms.CharField(
        label_suffix='',label='',
        widget = forms.Select(
            choices=Category_Choices,
            attrs={
                'class':'form-control',
            }
        )
    )
    class Meta:
        model = Articles
        fields = ('title','content','image',)

class CommentForm(forms.Form):
    content = forms.CharField(
        label_suffix='',label='',
        widget=forms.Textarea(
            attrs={
                'style':'height:150px;'
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)
