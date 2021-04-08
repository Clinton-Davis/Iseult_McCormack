from django import forms
from .models import productComment


class ProductCommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'rows': 4, }),
        label="Review")

    class Meta:
        model = productComment
        fields = ('content',)