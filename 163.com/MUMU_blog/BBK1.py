# coding=utf-8
__author__ = 'JACK_CHAN'
import urllib.request
import urllib.response
import urllib.parse
import re

"""
http://api.blog.163.com/yyyyy330/dwr/call/plaincall/BlogBeanNew.getBlogs.dwr
Request Method:POST
Content-Type:text/plain

设置参数，除了c0-param0、c0-param1和c0-param2外都一样。
c0-param0 ：博主的userId，例如yyyyy330的userId是“134612310”
c0-param1 ：返回博客数据的起始项，从0开始
c0-param2 ：一次返回博客的数量，最大值好像是500，具体多少我没有完全去试，600肯定不行，我一般设置500，600以上就不返回数据了。
如果一个博主写了超过500篇博客，那就可以分多次请求，只要合理设置c0-param1和c0-param2就可以。

"""


def get_blog_id(username, userID):
    url = 'http://api.blog.163.com/' + username + '/dwr/call/plaincall/BlogBeanNew.getBlogs.dwr'

    post = urllib.request.Request(url)
    post.add_header('User-Agent',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    post.add_header('Content-Type', 'text/plain')
    post.add_header('Referer', 'http://api.blog.163.com/crossdomain.html?t=20100205')
    paraDict = {
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
    paraDict['c0-param0'] = "number:" + userID
    paraDict['c0-param1'] = "number:" + str(0)
    paraDict['c0-param2'] = "number:" + str(500)
    data = urllib.parse.urlencode(paraDict)
    data = data.encode('utf-8')
    req = urllib.request.urlopen(post, data)
    bbk = req.read().decode('utf-8')
    batchID = re.findall('permaSerial="(.*?)"', bbk)
    print('取出来的长度:', len(batchID))

    """
    拼接链接,循环访问并取出标题即文本
    http://yyyyy330.blog.163.com/blog/static/134612310201612375310693/
    'http://' + username + '.blog.163.com/blog/static/' + batchID
    """
    blog_id = []
    [blog_id.append(i) for i in batchID if not i in blog_id]
    print('处理之后的长度：', len(blog_id))
    return blog_id


def main():
    pass

if __name__ == '__main__':
    print(get_blog_id('yyyyy330', '134612310'))
