import requests
from datetime import datetime
from bs4 import BeautifulSoup
from date_format import date_format

def parse_page(link):
    try:
        page = requests.get(link, requests=2)
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

    if soup.find_all("h1", class_="pagetitle__content-title") != []:
        title = soup.find_all("h1", class_="pagetitle__content-title")[0].get_text().strip()
    else:
        title = "Page Error: No Way To Get Title"

    if soup.find_all("h1", class_="pagetitle__content-title") != []:
        txt = soup.find_all("div", class_="usercontent")[1].get_text().strip()
    else:
        txt = "Page Error: No Way To Get Text"
    
    if soup.find_all("h1", class_="pagetitle__content-title") != []:
        posted_at = date_format(soup.find_all("div", class_="pagetitle__content-date")[0].get_text().strip())
    else:
        posted_at = datetime(1, 1, 1, 0, 0)

    return(title, txt, posted_at)

#print(parse_page("https://mosmetro.ru/press/news/archive/2021-08/4084/"))