import requests
from lxml import etree
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
qiushi = client['qiushi']
qiushi_info = qiushi['qiushi_info']
user_info = qiushi['user_info']

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}


def get_info(url):
    html = requests.get(url, headers=header)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//div[@class="col1"]/div')
    base_url = 'https://www.qiushibaike.com'
    for info in infos:
        id = info.xpath('div[1]/a[2]/h2/text()')[0] if len(info.xpath('div[1]/a[2]/h2/text()')) == 1 else '匿名用户'
        jug_sex = info.xpath('div[1]/div/@class')
        if len(jug_sex) == 0:
            sex = '不详'
            age = '不详'
        elif jug_sex[0] == 'articleGender manIcon':
            sex = '男'
            age = info.xpath('div[1]/div/text()')[0]
        else:
            sex = '女'
            age = info.xpath('div[1]/div/text()')[0]
        content = info.xpath('a[1]/div/span[1]/text()')[0]
        laugh = info.xpath('div[2]/span[1]/i/text()')[0]
        comment = info.xpath('div[2]/span[2]/a/i/text()')[0] if info.xpath('div[2]/span[2]/a/i/text()') else None
        user_url = base_url + info.xpath('div[1]/a[2]/@href')[0] if info.xpath('div[1]/a[2]/@href') else None
        data = {
            'id': id,
            'sex': sex,
            'age': age,
            'laugh': laugh,
            'comment': comment,
            'user_url': user_url,
            'content': content
        }
        qiushi_info.insert_one(data)
        print(data)
        if user_url == None:
            pass
        else:
            get_user_info(user_url)
    time.sleep(1)


def get_user_info(url):
    html = requests.get(url, headers=header)
    selector = etree.HTML(html.text)
    if selector.xpath('//div[@class="user-block user-setting clearfix"]'):
        pass
    else:
        fans = selector.xpath('//div[2]/div[3]/div[1]/ul/li[1]/text()')[0] if selector.xpath(
            '//div[2]/div[3]/div[1]/ul/li[1]/text()') else None
        topic = selector.xpath('//div[2]/div[3]/div[1]/ul/li[2]/text()')[0] if selector.xpath(
            '//div[2]/div[3]/div[1]/ul/li[2]/text()') else None
        qiushi = selector.xpath('//div[2]/div[3]/div[1]/ul/li[3]/text()')[0] if selector.xpath(
            '//div[2]/div[3]/div[1]/ul/li[3]/text()') else None
        comment_1 = selector.xpath('//div[2]/div[3]/div[1]/ul/li[4]/text()')[0] if selector.xpath(
            '//div[2]/div[3]/div[1]/ul/li[4]/text()') else None
        favour = selector.xpath('//div[2]/div[3]/div[1]/ul/li[5]/text()')[0] if selector.xpath(
            '//div[2]/div[3]/div[1]/ul/li[5]/text()') else None
        handpick = selector.xpath('//div[2]/div[3]/div[1]/ul/li[6]/text()')[0] if selector.xpath(
            '//div[2]/div[3]/div[1]/ul/li[6]/text()') else None
        martial_status = selector.xpath('//div[2]/div[3]/div[2]/ul/li[1]/text()')[0] if selector.xpath(
            '//div[2]/div[3]/div[2]/ul/li[1]/text()') else '不详'
        constellation = selector.xpath('//div[2]/div[3]/div[2]/ul/li[2]/text()')[0] if selector.xpath(
            '//div[2]/div[3]/div[2]/ul/li[2]/text()') else '不详'
        profession = selector.xpath('//div[2]/div[3]/div[2]/ul/li[3]/text()')[0] if selector.xpath(
            '//div[2]/div[3]/div[2]/ul/li[3]/text()') else '不详'
        home = selector.xpath('//div[2]/div[3]/div[2]/ul/li[4]/text()')[0] if selector.xpath(
            '//div[2]/div[3]/div[2]/ul/li[4]/text()') else '不详'
        qiushi_age = selector.xpath('//div[2]/div[3]/div[2]/ul/li[5]/text()')[0] if selector.xpath(
            '//div[2]/div[3]/div[2]/ul/li[5]/text()') else '不详'
        # print(fans,topic,qiushi,comment_1,favour,handpick,martial_status,constellation,profession,home,qiushi_age)
        data = {
            'fans': fans,
            'topic': topic,
            'qiushi': qiushi,
            'comment_1': comment_1,
            'favour': favour,
            'handpick': handpick,
            'martial_status': martial_status,
            'constellation': constellation,
            'profession': profession,
            'home': home,
            'qiushi_age': qiushi_age,
            'user_url': url
        }
        user_info.insert_one(data)
        print(data)


if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, 36)]
    for url in urls:
        print(url)
        get_info(url)
