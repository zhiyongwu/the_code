"""
一个HTML文件，找出里面的正文。
"""

import requests
from bs4 import BeautifulSoup


def get_html_body(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find("body").get_text()


if __name__ == '__main__':
    b = get_html_body('http://www.qq.com')
    print(b)
