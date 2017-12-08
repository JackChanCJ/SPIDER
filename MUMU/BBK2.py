# coding=utf-8
__author__ = 'JACK_CHAN'
import urllib.request
import urllib.response
import urllib.parse
import re
import time

username = 'yyyyy330'
userID = '134612310'
list = ['1346123102010230349995', '134612310201021473024840', '13461231020162153750135', '134612310201612375310693', '1346123102016123729456', '13461231020157139295269']
urllist = []
for i in list:
    url = 'http://' + username + '.blog.163.com/blog/static/' + i
    header_dict = {
        'Upgrade-Insecure-Requests':'1',
        'Referer':'http://yyyyy330.blog.163.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    req = urllib.request.Request(url, headers= header_dict)
    res = urllib.request.urlopen(req)
    # print (res.read().decode('gbk'))
    print (res.status)
    # if res.status == '200':
    # 服务器返回res，并对结果进行解码，查找相应的边界用非贪心模式爬取需要的内容
    # 此处不使用findall 是因为search在查找文本时，只要第一次找到文本后后面的文本都不查找了，提高查找效率
    title = re.findall('<input type="hidden" name="title" value="(.*?)" \/>', res.read().decode('gbk'))
    bodytext1 = re.findall('<div class="nbw-blog-start"><\/div>(.*?)<div class="nbw-blog-end"><\/div>', res.read().decode('gbk'))
    print (len(bodytext1))
    # 每次请求成功后，再间隔5秒钟向服务器发请求
    time.sleep(5)








def main():
    pass


if __name__ == '__main__':
    main()