"""
用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)http://tieba.baidu.com/p/2166231880
"""

import requests
from bs4 import BeautifulSoup
import os


def get_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_image(url):
    soup = get_page(url)
    all_pic = soup.find_all('img', {'class': 'BDE_Image'})
    for one in all_pic:
        yield one.attrs['src']


def download_img(url):
    package = '../download/image/'
    if not os.path.exists(package):
        os.makedirs(package)
    filename = package + url.split('/')[-1]
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)
        f.close()


if __name__ == '__main__':
    for each in get_image('http://tieba.baidu.com/p/2166231880'):
        download_img(each)
