import requests
import urllib.request
import bs4
import lxml

def get_image_link(keyword):
    req = requests.get("https://www.google.com/search?hl=jp&q=" + \
         keyword + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    link = soup.find_all("img")[1]
    pic = link['src']

    # x = []
    # for item in soup.find_all(attrs={"data-id":True}):
    #     x.append(item['data-id'])
    # print(x)

    return pic

        

## メモ
# 画像urlを開くと画像検索url + #imgrc={data-id}　となるのでなんとかdata-idをとればurlに直接飛べるのでは