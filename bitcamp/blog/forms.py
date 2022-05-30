from cProfile import label
from dataclasses import field
from pyexpat import model
from statistics import mode
from django import forms
from user.models import Author
from .models import Comment, Post


class CommentForm(forms.Form):
    text = forms.CharField(max_length=255, label='Comment Name No')
    author = forms.CharField(max_length=155)


class CommetModelForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4, 'class': 'form-control', 'placeholder': 'Comments here ...',
        'label': 'Cooments',
    }))

    class Meta:
        model = Comment
        fields = ('text',)


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
