from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget = forms.Textarea(attrs={
            'rows':3,
            'placeholder': 'Write your post ...',
            'id': 'body-post-form',
        })
    )
    
    
    class Meta:
        model = Post
        fields = ['body']
        
        
class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget = forms.Textarea(attrs={
            'rows':3,
            'placeholder': 'Write your comment ...'
        })
    )
    
    class Meta:
        model = Comment
        fields = ['comment']