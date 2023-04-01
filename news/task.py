import threading
import time
from news.scrape import Scrape


# Start Web scrape threading
def scrapeThreading():
    t1 = threading.Thread(target=Scrape, daemon=True)  # daemon thread runs in background
    t1.start()
    time.sleep(600)
    scrapeThreading()
