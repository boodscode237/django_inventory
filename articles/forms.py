from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        q = Article.objects.filter(title__icontains=title)
        if q.exists():
            self.add_error('title', f'<br>{title}</br> is already taken.')
        return data
    
    
    
class ArticleFormOld(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data # renders a dictionary
    #     title = cleaned_data.get('title')
    #     # print(type(title))
    #     # if title.lower().strip() == "title1":
    #     #     raise forms.ValidationError('This title is taken.')
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "title1":
            self.add_error('title', f'{title} is already taken.')
            # raise forms.ValidationError('This title is taken.')
        if 'office' in content or 'office' in title.lower():
            self.add_error('content', 'office cannot be in content')
        return cleaned_data