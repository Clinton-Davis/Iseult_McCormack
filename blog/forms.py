from django import forms
from .models import Blog, BlogComment, BlogCategory


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'category', 'overview', 'content', 'image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = BlogCategory.object.all()
        friendly_blog_name = [(c.id, c.get_friendly_blog_name())
                              for c in categories]

        placeholders = {
            'title': 'Your Blogs Title.',
            'overview': 'A little overview of the blog',
            'content': 'Write your Blog in here',
            'image': '200px x 200px',

        }

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['category'].choices = friendly_blog_name

        for field in self.fields:
            if field != 'category':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False


class BlogCommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4,
    }), label="")

    class Meta:
        model = BlogComment
        fields = ('content', )
