import threading
from django.urls import re_path, include
from .api import NewsList, AllNewsList
from .task import scrapeThreading
from .views import NewsView

# API URLS
api_patterns = ([
    re_path(r'^news/$', AllNewsList.as_view()),
    re_path(r'^news/(?P<searchitem>\w+)', NewsList.as_view()),
])

urlpatterns = [
    # News Page
    re_path(r'^news/$', NewsView, name='news'),
    re_path(r'^api/', include(api_patterns)),
]

# Initializing the threading of Scraping
threading.Thread(target=scrapeThreading, daemon=True).start()  # daemon thread runs in background
