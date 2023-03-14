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
    
    news_to_create = []
    
    for article in response['articles']:
        if all([article['title'],
                article['description'],
                article['url'],
                article['urlToImage'],
                article['publishedAt']
                ]):
            news_to_create.append(News(
                title=article['title'],
                description=article['description'],
                url=article['url'],
                urlToImage=article['urlToImage'],
                publishedAt=article['publishedAt']
            ))
    
    News.objects.bulk_create(news_to_create)
             
    return HttpResponse(response['articles'])