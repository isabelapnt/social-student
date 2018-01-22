from django import forms
from core.post.models import Post


class PostForm(forms.ModelForm):
    conteudo = forms.CharField(widget=forms.Textarea())
    titulo = forms.CharField(max_length=50, required=True)

    class Meta:
        model = Post
        fields = '__all__'
