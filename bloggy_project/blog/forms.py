from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'tag', 'image'] # this is required to match to column db
                                                        # removed views so end users couldn't mess with it