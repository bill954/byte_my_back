import requests
from django.shortcuts import render
from django_base.settings import NEWS_API_KEY
from django.http import HttpResponse

from news.models import News

def fetch_news(request):
    response = requests.get(F'https://newsapi.org/v2/everything?q=bitcoin&apiKey={NEWS_API_KEY}')
    if response.status_code != 200:
        return HttpResponse(response.status_code)
    response = response.json()
    
    for article in response['articles']:
        if all([article['title'],
                article['description'],
                article['url'],
                article['urlToImage'],
                article['publishedAt']
                ]):
            News.objects.create(
                title=article['title'],
                description=article['description'],
                url=article['url'],
                urlToImage=article['urlToImage'],
                publishedAt=article['publishedAt']
            )
             
    return HttpResponse(response['articles'])