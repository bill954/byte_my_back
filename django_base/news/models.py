from django.db import models

class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    url = models.CharField(max_length=255)
    urlToImage = models.CharField(max_length=255)
    publishedAt = models.DateTimeField()
    
    def __str__(self):
        return self.title