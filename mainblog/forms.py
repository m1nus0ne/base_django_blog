from .models import *
from django import forms

choices = list(Category.objects.all().values_list('name', 'name'))
choices_list = []


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'author')
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'author': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden', 'id': 'au'}),
                   'body': forms.Textarea(attrs={'class': 'form-control'}),
                   'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
                   }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'body': forms.Textarea(attrs={'class': 'form-control'}),
                   }


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'body')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'body': forms.Textarea(attrs={'class': 'form-control'}),
                   }
