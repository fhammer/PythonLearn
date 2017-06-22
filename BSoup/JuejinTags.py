#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen


# 单独查找每一个节点去获取数据
def get_juejin_tags(url):
    tags_page = urlopen(url)
    tags_soup = BeautifulSoup(tags_page, 'lxml')
    tags_page.close()
    tag_items = tags_soup.find_all(class_='title')
    print(len(tag_items))
    subscribe_counts = tags_soup.find_all(class_='meta subscribe')
    print(len(subscribe_counts))
    articles_counts = tags_soup.find_all(class_='meta article')
    print(len(articles_counts))
    # for item in tag_items:
    #     print(item.string)
    tag_infos = []
    for index in range(len(tag_items)):
        tag_name = tag_items[index].string
        subscribe_count = subscribe_counts[index].string.split(' ')[0]
        articles_count = articles_counts[index].string.split(' ')[0]
        info = {'name': tag_name, 'subscribe_count': subscribe_count, 'article_count': articles_count}
        tag_infos.append(info)
        print(info)
    return tag_infos


# 查找兄弟节点的方法获取数据
def get_juejin_tags_sibling(url):
    tags_page = urlopen(url)
    tags_soup = BeautifulSoup(tags_page, 'lxml')
    tags_page.close()
    tag_items = tags_soup.find_all(class_='title')
    print(len(tag_items))
    tag_infos = []
    for item in tag_items:
        tag_name = item.string
        # print(item.find_previous_sibling().get('style'))
        tag_sibling = item.parent.find_next_sibling()
        subscribe_count = tag_sibling.find('div', {'class': 'meta subscribe'}).string.split(' ')[0]
        articles_count = tag_sibling.find('div', {'class': 'meta article'}).string.split(' ')[0]
        info = {'name': tag_name, 'subscribe_count': subscribe_count, 'article_count': articles_count}
        tag_infos.append(info)
        print(info)
    return tag_infos


tags_all = get_juejin_tags_sibling('https://juejin.im/subscribe/all')
print(tags_all)
print(len(tags_all))
