import requests
from bs4 import BeautifulSoup
from collections import namedtuple


Article = namedtuple('Article', ["url", 
                                 "title", 
                                 "datetime", 
                                 "author", 
                                 "content",
                                 "tweeter_user", 
                                 "tweeter_url"])

class TechcrunchScraper(object):
    """
        A class used to scrap articles from techcrunch.com.
    """
    def __init__(self):
        self.base_url = "http://techcrunch.com"
    
    def find_articles(self, year, month, day):
        """
            Iterates through http://techcrunch.com/year/month/day/page/i/
            getting article links.
            Returns the article links strings on a list
        """
        articles_urls = []
        base_url = "%s/%s/%s/%s" % (self.base_url, year, month, day)
        for page_counter in range(1, 100):
            # iterates through article pages on the given date
            page_url = "%s/page/%s/" %(base_url, page_counter)
            html = requests.get(page_url)        
            if html.status_code == 200:
                try:
                    html_doc = html.content
                    soup = BeautifulSoup(html_doc, "html.parser")
                    article_lists = soup.findAll("ul", {"class":"river"})
                    for article_list in article_lists:
                        for article in article_list.findAll("li", {"class":"river-block"}):
                            articles_urls.append(article.get("data-permalink"))
                except Exception, e:
                    print "Couldn't get the list of article urls, error: %s" % e
                    break
            elif html.status_code == 404:
                # next page doesn't exist, this is not an unexpected error
                break
        return articles_urls
    
    
    def scrap_article(self, article_url):
        """
            Given an article url, extracts all info needed to create
            an Article object
        """
        html = requests.get(article_url)
        if html.status_code == 200:
            try:
                html_doc = html.content
                soup = BeautifulSoup(html_doc, "html.parser")
                
                # kill all script and style elements
                for script in soup(["script", "style"]):
                    script.extract()    # rip it out
                article_header = soup.find("header", {"class":"article-header"})
                article_url = html.url
                title = article_header.find("h1", {"class":"tweet-title"}).get_text()
                tweet_datetime = article_header.find("time", {"class":"timestamp"}).get("datetime")
                author = article_header.find("a", {"rel":"author"}).get_text()
                
                content = soup.find("div", {"class":"article-entry"}).get_text()
                try:
                    tweeter_user = article_header.find("span", {"class":"twitter-handle"}).find("a").get_text()
                    tweeter_url = article_header.find("span", {"class":"twitter-handle"}).find("a").get("href")
                except Exception, e:
                    tweeter_user, tweeter_url = "", ""
                
                article = Article(article_url, title, tweet_datetime, author, content, tweeter_user, tweeter_url)
                return article
            except Exception, e:
                print "Couldn't get the article data, error %s" % e
        

