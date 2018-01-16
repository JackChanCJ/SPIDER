# coding=utf-8
__author__ = 'JACK_CHAN'
import re
import requests
from wangyi import wangyiboke

wangyiboke_address = 'http://yyyyy330.blog.163.com/'

"""
    相册
    Request URL:http://yyyyy330.blog.163.com/album/
    Request Method:GET
    Status Code:200 OK
    Remote Address:61.164.158.2:80
"""


class album(wangyiboke):
    def __init__(self, username, id):
        wangyiboke.__init__(self, username, id)
        self.url = 'http://' + self.username + '.blog.163.com/album/'

    def __str__(self):
        return self.url

    def get_album_html(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'yyyyy330.blog.163.com',
            'Referer': 'http://yyyyy330.blog.163.com/blog',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        get = requests.get(self.albumurl, headers=headers)
        # print (get.encoding)  'GBK'
        # 得到的格式为 GBK，转换编码格式为 utf-8
        # get.encoding = 'utf-8'
        # 但是不需要转换
        albumhtml = get.text
        return albumhtml

    def get_album_names(self):
        title = re.findall('<a class="name iblock fw1 m2a tag" hidefocus="true" (.*?)</a>',
                           self.get_album_html())
        print(len(title))
        # <a class="name iblock fw1 m2a tag" hidefocus="true" href="#m=1&amp;aid=245402178&amp;p=1">123 木头人</a>

        return

    def get_current_page_album(self):
        return

    def get_total_pages(self):
        return


def main():
    B = album('yyyyy330', '134612310')
    B.get_album_names()


if __name__ == '__main__':
    main()

# http://img1.ph.126.net/NZdAE00-jFljNc707o4U1w==/1755277954867730329.jpg
# http://img1.ph.126.net/Tjg5cdeUKuN29ggnlCdo-g==/3403595418485653780.jpg
