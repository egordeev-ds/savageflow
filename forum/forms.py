from django import forms
from .models import Post, Answer

class PostForm(forms.ModelForm):
    content = forms.CharField(required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content','image')