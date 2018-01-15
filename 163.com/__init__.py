# coding=utf-8
__author__ = 'JACK_CHAN'
import re
import requests

"""
http://api.blog.163.com/yyyyy330/dwr/call/plaincall/BlogBeanNew.getBlogs.dwr
Request Method:POST
Content-Type:text/plain

设置参数，除了c0-param0、c0-param1和c0-param2外都一样。
c0-param0 ：博主的userId，例如yyyyy330的userId是“134612310”
c0-param1 ：返回博客数据的起始项，从0开始
c0-param2 ：一次返回博客的数量，最大值好像是500，具体多少我没有完全去试，600肯定不行，我一般设置500，600以上就不返回数据了。
如果一个博主写了超过500篇博客，那就可以分多次请求，只要合理设置c0-param1和c0-param2就可以。
paradict['c0-param2']的值不能大于500，微博文章总量大于500的需要分多次获取

"""

class wangyiboke:
    def __init__(self, username, id):
        self.username = username
        self.id = id
        self.blogurl = 'http://api.blog.163.com/' + self.username + '/dwr/call/plaincall/BlogBeanNew.getBlogs.dwr'
        self.photourl = 'http://' + self.username + '.blog.163.com/album/'


    def get_blog_html(self):
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
        post = requests.post(self.blogurl, headers=headers, data=paradict)
        # print (post.encoding)     'ISO-8859-1'
        # r.content 可以找到所用的编码格式，再用r.encoding设置编码值
        # 得到的格式为 ISO-8859-1，转换编码格式为 utf-8
        post.encoding = 'utf-8'
        bloghtml = post.text
        return bloghtml

    # 使用正则表达式来处理bloghmtl
    def re_blog_html(self):
        batchID = re.findall('permaSerial="(.*?)"', self.get_blog_html())
        L = []
        [L.append(i) for i in batchID if i not in L]
        return L

# Request URL:http://yyyyy330.blog.163.com/album/
# Request Method:GET
# Status Code:200 OK
# Remote Address:61.164.158.2:80
    def get_photo_html(self):
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
        get = requests.get(self.photourl, headers= headers)
        # print (get.encoding)  'GBK'
        # 得到的格式为 GBK，转换编码格式为 utf-8
        # get.encoding = 'utf-8'
        # 但是不需要转换
        photohtml = get.text
        print (photohtml)
        return photohtml



def main():
    B = wangyiboke('yyyyy330', '134612310')
    print (B.blogurl)
    print (B.photourl)
    B.get_photo_html()

    pass

if __name__ == '__main__':
    main()
