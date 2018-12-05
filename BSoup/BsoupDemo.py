#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def readUrl(strUrl):
    with request.urlopen(strUrl) as f:
        htmlData = f.read()
        print(htmlData)
        return htmlData


html_atag = """<html><body><p>Test html a tag example</p>
<a href="http://www.allitebook.com">Home</a>
<a href="http://www.allitebook.com/books">Books</a>
</body>
</html>"""
soup = BeautifulSoup(html_atag, "html5lib")

print(soup.prettify())
for x in soup.find_all('a'):
    print(x.attrs['href'])
    print(x.get('href'))

data = readUrl('http://www.jianshu.com')
bs4Soup = BeautifulSoup(data, 'lxml')
soup.prettify()
for x in bs4Soup.find_all('a'):
    print(x.attrs['href'])
    print(x.get('href'))
