# coding=utf-8
__author__ = 'JACK_CHAN'
import re
import requests
from wangyi import wangyiboke

wangyiboke_address = 'http://yyyyy330.blog.163.com/'

"""
    相册
    Request URL:http://s2.ph.126.net/KgQkN5OyiwP0L5IGpHgUAA==/266081839343804.js
    Request Method:GET
    Status Code:200 OK (from disk cache)
    Remote Address:123.53.139.232:80
    self.text获取的数据格式
{
    id: 193186286,
    name: '林中漫步',
    s: 3,
    desc: '',
    st: 5,
    au: 2,
    count: 15,
    t: 1260883742140,
    ut: 1263138278365,
    cvid: 5673060057,
    curl: '2/ZBaHoMf-NHjwV6xlq7Yr3A==/3025855999641186443.jpg',
    surl: '2/Q2yQGWF9f9Wl-kZ2QHAbCw==/3025855999641186446.jpg',
    lurl: '0/0-YOfu2Y7j3dYKKznL0pAw==/1766255478861007467.jpg',
    dmt: 2106086069,
    alc: true,
    kw: '',
    purl: ''
},

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

    def get_album_aid(self):
        # self.album_id 正则处理self.text，获取相册的id
        self.album_aid = re.findall("\{id:(.*?),name:'", self.text)
        return self.album_aid

    def get_album_url(self):
        self.get_album_aid()
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
        for i in self.album_aid:
            # print (i, id.index(i) + 1)
            album_url = 'http://%s.blog.163.com/album/#m=1&aid=%s&p=1' % (self.username, i)
            self.album_url.append(album_url)
        return self.album_url

    def get_album_purl(self):
        self.album_purl = re.findall("purl:'(.*?)'", self.text)
        return self.album_purl

    def get_album_name(self):
        # self.album_name 正则处理self.text，获取相册的name
        self.album_name = re.findall("name:'(.*?)'", self.text)
        # print("相册name的个数：%s" % len(self.album_name))
        # print(self.album_name)
        return self.album_name

    def zip_album(self):
        # 组成一个字典，key为相册名，value为相册链接
        self.get_album_name()
        self.get_album_url()
        self.zip_album = dict(zip(self.album_name, self.album_url))
        return self.zip_album




class child_album(album):
    def __init__(self, username, id, aid):
        album.__init__(self, username, id)

    def __str__(self):
        self.album_url = 'http://%s.blog.163.com/album/#m=1&aid=%s&p=1' % (self.username, self.aid)
        referer = 'http://%s.blog.163.com/album' % self.username
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Content-Type': 'text/plain',
            'Referer': referer
        }
        self.album_text = requests.get(self.album_url, headers=headers).text
        return self.album_text

    def child_album_url(self):
        self.pid = re.findall('cvid: (.*?)', self.text)
        return self.pid

    def get_child_album_Ctime(self):

        return

    def get_child_album_name(self):

        return

    def get_child_album_pic(self):
        return "abc"



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
    print(B.get_album_aid())
    # print(B.text)
    # print (B.get_album_name())
    # print (B.get_album_url())

    C = child_album('yyyyy330', '134612310', '261006686')
    print(C.url)



if __name__ == '__main__':
    main()

