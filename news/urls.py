from django.urls import path
import threading
from news.task import scrapeThreading
from news.api import NewsList, AllNewsList

urlpatterns = [
    path('news', AllNewsList.as_view()),
    path('news/<searchitem>', NewsList.as_view()),
]

# Initializing the threading of Scraping
threading.Thread(target=scrapeThreading, daemon=True).start()       # daemon thread runs in background