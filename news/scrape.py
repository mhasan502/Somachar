import timeit
import threading
import traceback

import requests
from bs4 import BeautifulSoup
#from news.models import News


# checking if that news link exists on database
def CheckIfExist(news_link):
    # num_of_news = News.objects.filter(newslink=news_link).count()
    # return num_of_news
    return 0


# Main news page to bring more news
def FirstRequest(url):
    res = requests.get(url)
    return BeautifulSoup(res.text, 'html.parser')


# collect news links
def CollectLinks(soup, find_class, name):
    list_of_link = []
    for findLink in soup.find_all(find_class):
        link = findLink.get('href')
        if len(str(link)) >= 45 and name.lower() in link:
            list_of_link.append(link)
    links = list(dict.fromkeys(list_of_link))  # remove same link
    links.reverse()
    return links


# save to database
def SaveToDB(head, image_link, news_link, desc, name):
    # if desc != '' and len(head) < 90:
    #     news = News(heading=head, imagelink=image_link, newslink=news_link, details=desc, papername=name)
    #     news.save()
    pass


# web scraping Jugantor
def Jugantor():
    name = 'Jugantor'
    url = 'https://www.jugantor.com/all-news'

    find_class = 'a', {'class': 'text-decoration-none'}
    soup = FirstRequest(url)
    links = CollectLinks(soup, find_class, name)

    while len(links) > 0:
        news_link = links.pop()
        try:
            if CheckIfExist(news_link) == 0:
                news_url = requests.get(news_link)
                soup = BeautifulSoup(news_url.text, 'html.parser')

                head_div = soup.find('h3', {'class': 'font-weight-bolder'})
                head = head_div.getText()

                image_div = soup.find('img', {'class': 'figure-img img-fluid rounded-0'})
                image_link = image_div.get('src')

                desc = ''
                for i in soup.find_all('div',
                                       {'class': 'IfTxty news-element-text text-justify my-2 pr-md-4 text-break'}):
                    desc = i.getText().replace("\n", "")

                SaveToDB(head, image_link, news_link, desc, name)
            else:
                break
        except Exception:
            continue


# web scraping Samakal
def Samakal():
    name = 'Samakal'
    url = 'https://samakal.com/list/all'

    find_class = 'a', {'class': 'link-overlay'}
    links = CollectLinks(FirstRequest(url), find_class, name)

    while len(links) > 0:
        news_link = links.pop()
        try:
            if CheckIfExist(news_link) == 0:
                news_url = requests.get(news_link)
                soup = BeautifulSoup(news_url.text, 'html.parser')

                head_div = soup.find('h1', {'class': 'detail-headline'})
                head = head_div.getText()

                image_div = soup.find('div', {'class': 'image-container image rel-soci'})
                image = image_div.find('img', {'class': None})
                image_link = image.get('src')

                desc = ''
                body = soup.find('div', {'class': 'description'})
                for i in body.find_all('p'):
                    desc += i.getText().replace("\n", "")

                SaveToDB(head, image_link, news_link, desc, name)
            else:
                break
        except Exception:
            continue


# web scraping Ittefaq
def Ittefaq():
    name = 'Ittefaq'
    url = 'https://www.ittefaq.com.bd/latest-news'

    find_class = 'a', {'class': None}
    links = CollectLinks(FirstRequest(url), find_class, name)

    while len(links) > 0:
        news_link = links.pop()
        if news_link[0] == '/' and news_link[1] == '/':
            news_link = "https:" + news_link
        try:
            if CheckIfExist(news_link) == 0:
                news_url = requests.get(news_link)
                soup = BeautifulSoup(news_url.text, 'html.parser')

                head_div = soup.find('h1', {'class': 'title mb10'})
                head = head_div.getText()

                image_div = soup.find('div', {'class': 'featured_image'})
                print(image_div)
                image = image_div.find('a', {'class': 'jw_media_holder media_image alignfull pop-media-holder pop-active'})
                image_link = "https://www.ittefaq.com.bd" + image.get('src')
                print(image_link)

                desc = ''
                body = soup.find('div', {'id': 'dtl_content_block'})
                for i in body.find_all('p'):
                    desc += i.getText().replace("\n", "")

                SaveToDB(head, image_link, news_link, desc, name)
            else:
                break
        except Exception:
            traceback.print_exc()
            continue


# Start scraping
def Scrape():
    start = timeit.default_timer()

    print("______________Initialized Scrape_________________")
    # p1 = threading.Thread(target=Jugantor())
    # p2 = threading.Thread(target=Samakal())
    p3 = threading.Thread(target=Ittefaq())

    # p1.start()
    # p2.start()
    p3.start()

    stop = timeit.default_timer()
    print('Time: ', stop - start)


if __name__ == '__main__':
    Scrape()