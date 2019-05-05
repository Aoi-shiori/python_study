import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
import re



def get_page_index():
    data={
    'aid': '24',
    'app_name':'web_search',
    'offset':'0',
    'format':'json',
    'keyword': '街拍',
    'autoload': 'true',
    'count': '20',
    'en_qc': '1',
    'cur_tab': '1',
    'from': 'search_tab',
    'pd': 'synthesis',
    'timestamp': '1557041655435'
    }

    headers = {
        ':authority': 'www.toutiao.com',
        ':method': 'GET',
        ':path': '/ search /?keyword = % E8 % A1 % 97 % E6 % 8B % 8D',
        ': scheme': 'https',
        'accept': '''text / html, application / xhtml + xml, application / xml;
        q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;
        v = b3''',
        'accept - encoding': 'gzip, deflate, br',
        'accept - language': '''zh - CN, zh;
        q = 0.9, zh - TW;
        q = 0.8, en;
        q = 0.7''',
        'cache - control': 'max - age = 0',
        'cookie': '''tt_webid = 6644299735950509575;
        UM_distinctid = 168302
        f23c3b3 - 01e620701
        a3efa - b781e3e - 100200 - 168302
        f23c41cf;
        csrftoken = 5087
        b3c4f8ddd945ec6b93afc3b23487;
        tt_webid = 6644299735950509575;
        WEATHER_CITY = % E5 % 8
        C % 97 % E4 % BA % AC;
        __tasessionId = xnswfanz21557041514753;
        CNZZDATA1259612802 = 725458634 - 1546995716 - % 7
        C1557041329;
        s_v_web_id = 9e1
        d0e8ff03fb73b889844e244788603''',
        'dnt': '1',
        'referer': 'https: // landing.toutiao.com /',
        'upgrade - insecure - requests': '1',
        'user - agent': '''Mozilla / 5.0(WindowsNT10.0;Win64;
        x64) AppleWebKit / 537.36(KHTML, like
        Gecko) Chrome / 74.0
        .3724
        .8
        Safari / 537.36''',

    }

    url='https://www.toutiao.com/api/search/content/?'+urlencode(data)
    try:
        response =requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求出错")
        return  None

def parse_url_index(html):
    data = json.loads(html)
    if data and "data" in data.keys():
        for item in data.get("data"):
            yield item.get("article_url")#找到open_url的键值，返回
            print('获得的url地址是',item)

def get_url_details(url):
    try:
        response =requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求出错",url)
        return  None

def parse_url_details(html):
    soup =BeautifulSoup(html, 'lxml')
    title =soup.select('title')[0].get_text()
    image_rex =re.compile('gallery: JSON.parse.(.*?)\)' , re.S)
    result =re.search(image_rex,html)
    if result:
        print(result.group(1))


def main_run():
    html = get_page_index()
    print(html)
    for url in parse_url_index(html):
        print('找到的url是', url)
        #html =parse_url_details(url)


if __name__=='__main__':
    main_run()
