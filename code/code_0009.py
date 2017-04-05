"""
一个HTML文件，找出里面的链接。
"""
import requests
from bs4 import BeautifulSoup


def get_all_href(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    for a in soup.find_all('a'):
        if 'href' in a.attrs:
            yield a.attrs['href']


if __name__ == '__main__':
    for each in get_all_href("http://www.qq.com"):
        print(each)
