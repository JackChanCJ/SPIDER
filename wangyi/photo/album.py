# coding=utf-8
__author__ = 'JACK_CHAN'
import re
import json
import requests
from wangyi import wangyiboke

wangyiboke_address = 'http://yyyyy330.blog.163.com/'

"""
    相册
    Request URL:http://s2.ph.126.net/KgQkN5OyiwP0L5IGpHgUAA==/266081839343804.js
    Request Method:GET
    Status Code:200 OK (from disk cache)
    Remote Address:123.53.139.232:80
"""


class album(wangyiboke):
    def __init__(self, username, id):
        wangyiboke.__init__(self, username, id)
        self.url = 'http://s2.ph.126.net/KgQkN5OyiwP0L5IGpHgUAA==/266081839343804.js'

    def __str__(self):
        return self.url

    def get_all_album_url(self):
        host = 's2.ph.126.net'
        referer = 'http://%s.blog.163.com/album' % self.username
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Host': host,
            'Referer': referer,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        text = requests.get(self.url, headers=headers).text
        # print (get.encoding)  'GBK'
        # 得到的格式为 GBK，转换编码格式为 utf-8
        # get.encoding = 'utf-8'
        # 但是不需要转换
        data = re.findall('{.*?},', text)
        # for i in data:
        #     j = re.findall(u'[\u4e00-\u9fa5]+', u'%s' %i)
        #     print (data.index(i))
        #     print (j)
        #     print (i)
        # {id:193186286,name:'林中漫步',s:3,desc:'',st:5,au:2,count:15,   。。。。。。等等等等。。。。。},
        id = re.findall('\{id:(.*?),name', text)
        allalbumurl = []
        for i in id:
            # print (i, id.index(i) + 1)
            albumurl = 'http://%s.blog.163.com/album/#m=1&aid=%s&p=1' % (self.username, i)
            print(albumurl)
            allalbumurl = allalbumurl.append()
        name = re.findall("name:'(.*?)'", text)

        # idname = dict(zip(id, name))
        # print (len(idname))
        # http://yyyyy330.blog.163.com/album/#m=1&aid=268809115&p=1


        return text

    def parse_album(self):

        return


    def get_total_pages(self):

        return


def main():
    B = album('yyyyy330', '134612310')
    B.get_all_album_url()


if __name__ == '__main__':
    main()

