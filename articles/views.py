from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article

# Create your views here.

def article_detail_view(request, id:int=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    
    return render(request, "articles/detail.html", context=context)

def article_search_view(request):
    query_dict = request.GET
    query = query_dict.get('query')
    
    try:
        query = int(query_dict.get('query'))
    except:
        query = None
        
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        'object': article_obj
    }
    return render(request, 'articles/search.html', context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
            article_object = form.save()
            # context['form']
            # title, content = form.cleaned_data.get('title'), form.cleaned_data.get('content')
            # print(title, content)
            # article_object = Article.objects.create(title=title, content=content)
            context['object'], context['created'] = article_object, True
    return render(request, "articles/create.html", context=context)

# @login_required
# def article_create_view(request):
#     context = {"form": ArticleFrom()}
#     context['form'] = form
#     if request.method == 'POST':
#         form = ArticleFrom(request.POST)
        
#         if form.is_valid():
#             title, content = form.cleaned_data.get('title'), form.cleaned_data.get('content')
#             print(title, content)
#             article_object = Article.objects.create(title=title, content=content)
#             context['object'], context['created'] = article_object, True

#     return render(request, "articles/create.html", context=context)