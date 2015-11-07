import simplejson

from django.http import HttpResponse

from .models import Article

INDEX_ARTICLES_NUMBER = 100

def articles_cursor_to_json(cursor):
    articles = [article.article_dict() for article in cursor]
    return simplejson.dumps(articles)

def index(request):
    """
        returns the last INDEX_ARTICLES_NUMBER articles
    """
    articles = Article.objects.order_by('-pub_date')[:INDEX_ARTICLES_NUMBER]
    response = articles_cursor_to_json(articles)
    return HttpResponse(response, content_type="application/json")

def articles_by_year(request, year):
    """
        returns all articles of the given year
    """
    try:
        articles = Article.objects.filter(pub_date__year=year)
        response = articles_cursor_to_json(articles)
    except ValueError:
        response = []
    return HttpResponse(response, content_type="application/json")

def articles_by_month(request, year, month):
    """
        returns all articles of the given year/month
    """
    try:
        articles = Article.objects.filter(pub_date__year=year).filter(pub_date__month=month)
        response = articles_cursor_to_json(articles)
    except ValueError:
        response = []
    return HttpResponse(response, content_type="application/json")

def articles_by_day(request, year, month, day):
    """
        returns all articles of the given year/month/day
    """
    try:
        articles = Article.objects.filter(pub_date__year=year).filter(pub_date__month=month).filter(pub_date__day=day)
        response = articles_cursor_to_json(articles)
    except ValueError:
        response = []
    return HttpResponse(response, content_type="application/json")
