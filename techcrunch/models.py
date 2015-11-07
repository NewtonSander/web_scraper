from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=300)
    tweeter_user = models.CharField(max_length=100)
    tweeter_url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name



class Article(models.Model):
    author = models.ForeignKey(Author)
    url = models.CharField(max_length=2000)
    title = models.CharField(max_length=2000)
    content = models.TextField()
    pub_date = models.DateField()
    
    def __str__(self):
        return self.title