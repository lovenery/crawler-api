import requests
from bs4 import BeautifulSoup
import re

re_imgur_com = re.compile('https?:\/\/(?:i\.)?imgur\.com\/\w+')

def start(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select('div.title a')

    results = []
    for a in articles:
        result = []
        url = 'https://www.ptt.cc' + a['href']
        result.append(a.text)
        result.append(url)
        page = requests.get(url)
        imgurs = re_imgur_com.findall(page.text)
        for image in set(imgurs):
            result.append(image)
        if len(result) > 1 and "[公告]" not in result[0] and "小天使" not in result[0]:
            results.append(result)

    paging = soup.select('div.btn-group-paging a')
    next_url = 'https://www.ptt.cc' + paging[1]['href']

    return next_url, results

