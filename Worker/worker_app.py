import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup

from page_parser import parse_page

from create_table import create_table_parsed_pages
from search import search_link
from insert import insert_pages

# создаём таблицу
create_table_parsed_pages()

while True:
    try:
        page = requests.get('https://mosmetro.ru/press/news/archive/', timeout=1)
        page.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)

    soup = BeautifulSoup(page.text, 'html.parser')

    for a in soup.find_all('a', href=True):
        if ((a['href'][0:7] == '/press/') and (len(a['href'])>15)) :
            
            img_link = "https://mosmetro.ru"+a.find_next("img")['src']
            link = "https://mosmetro.ru"+a['href']

            if search_link(link) == False:
                title, txt, posted_at = parse_page(link)
                insert_pages(link, title, txt, img_link, posted_at, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))            

    time.sleep(10*60)