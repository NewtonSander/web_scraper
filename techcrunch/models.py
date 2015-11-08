from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=300, db_tablespace="indexes")
    tweeter_user = models.CharField(max_length=100, db_tablespace="indexes")
    tweeter_url = models.CharField(max_length=200, db_tablespace="indexes")

    def author_dict(self):
        return {"name":self.name,
                "tweeter_user":self.tweeter_user,
                "tweeter_url":self.tweeter_url}


class Article(models.Model):
    author = models.ForeignKey(Author)
    url = models.CharField(max_length=2000, db_tablespace="indexes")
    title = models.CharField(max_length=2000, db_tablespace="indexes")
    content = models.TextField(db_tablespace="indexes")
    pub_date = models.DateField(db_tablespace="indexes")
    
    def article_dict(self):
        return {
                "author":self.author.author_dict(),
                "url":self.url,
                "title":self.title,
                "pub_date":self.pub_date.isoformat(),
                "content":self.content,
                }
    
    