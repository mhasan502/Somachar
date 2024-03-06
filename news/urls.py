import threading
from django.urls import path, include
from .api import NewsList, AllNewsList, NewsDetails
from .task import scrape_threading
from .views import NewsListView

# API URLS
api_patterns = ([
    path('news/', AllNewsList.as_view()),
    path('news/<str:searchitem>', NewsList.as_view()),
    path('news/details/<int:news_id>/', NewsDetails.as_view()),
])

urlpatterns = [
    # News Page
    path('news/', NewsListView.as_view(), name='news'),
    path('api/', include(api_patterns)),
]

# Initializing the threading of Scraping
threading.Thread(target=scrape_threading, daemon=True).start()  # daemon thread runs in background
