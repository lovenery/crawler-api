import requests
from bs4 import BeautifulSoup

def president():
    response = requests.get('http://www.president.gov.tw/Page/37')
    soup = BeautifulSoup(response.text, 'html.parser')

    header = soup.select('.content')
    content = soup.select('.SearchHightLight')

    return header[0].get_text(), content[0].get_text(separator='<br>')
