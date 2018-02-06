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
        self.text = requests.get(self.url, headers=headers).text

    def __str__(self):
        return self.url

    def get_album_url(self):

        # print (get.encoding)  'GBK'
        # 得到的格式为 GBK，转换编码格式为 utf-8
        # get.encoding = 'utf-8'
        # 但这里不需要转换
        # data正则处理的是
        # data = re.findall('{.*?},', text)
        # print (""len(data))
        # {id:193186286,name:'林中漫步',s:3,desc:'',st:5,au:2,count:15,   。。。。。。等等等等。。。。。},

        # 通过用户名，相册id，拼接相册url，self.album_url相册中所有的url
        self.album_url = []
        for i in self.album_id:
            # print (i, id.index(i) + 1)
            album_url = 'http://%s.blog.163.com/album/#m=1&aid=%s&p=1' % (self.username, i)
            self.album_url.append(album_url)
        print("相册url的长度：%s" % len(self.album_url))
        print(self.album_url)

        # idname = dict(zip(id, name))
        # print (len(idname))
        # http://yyyyy330.blog.163.com/album/#m=1&aid=268809115&p=1

        return self.album_url

    def get_album_id(self):
        # self.album_id 正则处理self.text，获取相册的id
        self.album_id = re.findall('\{id:(.*?),name', self.text)
        print("相册id的个数：%s" % len(self.album_id))
        print(self.album_id)
        return self.album_id

    def get_album_name(self):
        # self.album_name 正则处理self.text，获取相册的name
        self.album_name = re.findall("name:'(.*?)'", self.text)
        print("相册name的个数：%s" % len(self.album_name))
        print(self.album_name)
        return self.album_name

    def get_album_Ctime(self):

        return

    def zip_album(self):
        self.zip_album = dict(zip(self.album_name, self.album_url))
        return self.zip_album


    def get_total_pages(self):

        return


class child_album(album):
    def __init__(self, username, id):
        album.__init__(self, username, id)

    def get_album_Ctime(self):
        return

    def get_album_name(self):
        return

    def get_album_pic(self):
        return


class pic(child_album):
    def __init__(self, username, id):
        child_album.__init__(self, username, id)

    def pic_name(self):
        return

    def pic_Ctime(self):
        return

    def pic_file(self):
        return

def main():
    B = album('yyyyy330', '134612310')
    print(B.zip_album())
    # B.get_album_id()
    # B.get_album_name()
    # B.get_album_url()
    C = child_album('yyyyy330', '134612310')
    print(C.url)

if __name__ == '__main__':
    main()

