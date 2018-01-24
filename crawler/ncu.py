import requests
from bs4 import BeautifulSoup

def single_ann(category_str):
    response = requests.get('http://www.csie.ncu.edu.tw/announcement/category/' + category_str)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.select_one('h3')
    links = soup.select('.card .link')

    ann_lists = []
    for a_tag in links:
        tmp = []
        tmp.append('http://www.csie.ncu.edu.tw' + a_tag['href'])
        tmp.append(a_tag.select_one('.item-title').text)
        tmp.append(a_tag.select_one('.item-time').text)
        ann_lists.append(tmp)

    ann_dict = {}
    ann_dict['ann_title'] = title.text
    ann_dict['ann_lists'] = ann_lists

    return ann_dict

def csie_category():
    data = []
    # data.append(single_ann(category_str='得獎訊息')) # useless
    data.append(single_ann(category_str='徵才訊息'))
    # data.append(single_ann(category_str='招生快訊')) # useless
    data.append(single_ann(category_str='演講公告'))
    data.append(single_ann(category_str='活動快訊'))
    data.append(single_ann(category_str='課程訊息'))
    data.append(single_ann(category_str='系辦公告'))
    return data

def csie_all(page):
    if page is None or page == '':
        page = 3
    else:
        page = int(page)
    if page < 3 or page > 175:
        page = 3

    data = []
    for i in range(1, page):
        url = 'http://www.csie.ncu.edu.tw/announcement/page/' + str(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = soup.select('.card .link')

        for a_tag in links:
            tmp = []
            tmp.append('http://www.csie.ncu.edu.tw' + a_tag['href'])
            tmp.append(a_tag.select_one('.item-title').text)
            tmp.append(a_tag.select_one('.item-time').text)
            data.append(tmp)

    return data