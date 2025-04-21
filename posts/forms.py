from django import forms

from posts.models import Posts, Comment


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['user', 'title', 'content']
        # user = forms.CharField(max_length=25)
        # title = forms.CharField(max_length=128)
        # content = forms.CharField(max_length=128)
        # created_ad = forms.DateField


class CommentForm(forms.Form):
    # user = forms.CharField(max_length=25)
    # post = forms.CharField(max_length=128)
    # content = forms.CharField(max_length=128)
    # created_ad = forms.DateField

    class Meta:
        model = Comment
        fields = ['user', 'post', 'content']
