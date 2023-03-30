from django.urls import path
import threading
from .task import scrapeThreading
from .api import NewsList, AllNewsList
from .views import news_view


urlpatterns = [
    path('news', AllNewsList.as_view()),
    path('news/<searchitem>', NewsList.as_view()),
    # News Page
    path("news/", news_view, name='news'),
]

# Initializing the threading of Scraping
threading.Thread(target=scrapeThreading, daemon=True).start()       # daemon thread runs in background
