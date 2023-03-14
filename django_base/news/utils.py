import random
from news.models import News

# Creating a function to get random news

def get_random_news():
    all_news = News.objects.all()
    selected_news = random.choices(all_news, k=4)
    # return one new 0 for the main frame, and the rest appart
    return (selected_news[0], selected_news[1:])