from __future__ import absolute_import

from celery import shared_task

from .scraper import TechcrunchScraper
from .models import Article, Author

scraper = TechcrunchScraper()

@shared_task
def find_articles(year, month, day):
    """
        Finds and saves on django DB all articles of the given date
    """
    articles_urls = scraper.find_articles(year, month, day)
    for article_url in articles_urls:
        article = scraper.scrap_article(article_url)
        if article:
            author_db, created = Author.objects.get_or_create(name=article.author, 
                               tweeter_user=article.tweeter_user, 
                               tweeter_url=article.tweeter_url)
            
            author_db.save()
            article_db, created = Article.objects.get_or_create(author=author_db,
                                                                url=article.url,
                                 title=article.title,
                                 content=article.content,
                                 pub_date=article.datetime)                
            article_db.save()