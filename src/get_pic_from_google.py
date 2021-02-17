import requests
import bs4
import lxml

def get_image_link(keyword):
    req = requests.get("https://www.google.com/search?hl=jp&q=" + \
         keyword + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    link = soup.find_all("img")[1]
    pic = link['src']
    return pic
