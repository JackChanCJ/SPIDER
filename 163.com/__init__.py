# coding=utf-8
__author__ = 'JACK_CHAN'
import re
import requests


class wangyiboke:
    def __init__(self, username, id):
        self.username = username
        self.id = id

    def get_blog_html(self):
        blogurl = 'http://api.blog.163.com/' + self.username + '/dwr/call/plaincall/BlogBeanNew.getBlogs.dwr'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Content-Type': 'text/plain',
            'Referer': 'http://api.blog.163.com/crossdomain.html?t=20100205'
        }
        paradict = {
            'callCount': '1',
            'scriptSessionId': '${scriptSessionId}187',
            'c0-scriptName': 'BlogBeanNew',
            'c0-methodName': 'getBlogs',
            'c0-id': '0',
            'c0-param0': '134612310',
            'c0-param1': '0',
            'c0-param2': '20',
            'batchId': '1'
        }
        paradict['c0-param0'] = "number:" + self.id
        paradict['c0-param1'] = "number:" + str(0)
        paradict['c0-param2'] = "number:" + str(20)
        blogpost = requests.post(blogurl, headers=headers, data=paradict)
        # print (blogpost.encoding)     'ISO-8859-1'
        # r.content 可以找到所用的编码格式，再用r.encoding设置编码值
        # 得到的格式为 ISO-8859-1，转换编码格式为 utf-8
        blogpost.encoding = 'utf-8'
        bloghtml = blogpost.text
        return bloghtml

    def re_blog_html(self, get_blog_html):
        pass

    def get_photo_html(self):
        return


def main():
    B = wangyiboke('yyyyy330', '134612310')
    B.get_blog_html()
    pass

if __name__ == '__main__':
    main()
