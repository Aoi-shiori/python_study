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
    'offset':'20',
    'format':'json',
    'keyword': '街拍',
    'autoload': 'true',
    'count': '20',
    'en_qc': '1',
    'cur_tab': '1',
    'from': 'search_tab',
    'pd': 'synthesis',
    #'timestamp': '1556249200270'
    }


    url='https://www.toutiao.com/api/search/content/?'+urlencode(data)
    try:
        response =requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求出错")
        return  None

def parse_url_index(html):
    data = json.loads(html)
    print('转换后的data数据是', data)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')#找到article_url的键值，返回

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
