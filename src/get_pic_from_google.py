import requests
import bs4

def get_image_link(keyword):
    req = requests.get("https://www.google.com/search?hl=jp&q=" + \
         keyword + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    links = soup.find_all("img") # 最初の画像だけをとって来るように変更したい
    link = links[1]
    return link


a = get_image_link("動物")
print(a)