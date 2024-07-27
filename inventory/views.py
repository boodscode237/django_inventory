import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import random

from articles.models import Article



def home_view(request):
    """
    This function is responsible for rendering the home page of the website.
    It retrieves a random article, generates a list, fetches all articles,
    prepares a context dictionary, renders the context to a HTML string,
    and returns an HttpResponse object with the HTML string.

    Parameters:
    request (HttpRequest): The incoming request object.

    Returns:
    HttpResponse: An HttpResponse object containing the rendered HTML string.
    """

    # Retrieve a random article
    article_obj = Article.objects.get(id=random.randint(1,2))

    # Define a list
    my_list = [120, 584, 654, 85]

    # Fetch all articles
    articles = Article.objects.all()

    # Prepare the context dictionary
    context = {
        "my_list_str": my_list,
        "current_date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "shop_name": "ETS ELOUNDOU",
        "articles": articles,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }

    # Return an HttpResponse object with the HTML string
    return render(request, "home-view.html", context=context)

