import threading
import time
from .scrape import scrape


def scrape_threading():
    """
    Start Web scrape threading
    """
    t1 = threading.Thread(target=scrape, daemon=True)  # daemon thread runs in background
    t1.start()
    time.sleep(600)
    scrape_threading()
