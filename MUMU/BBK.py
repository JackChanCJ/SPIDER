# coding=utf-8
__author__ = 'JACK_CHAN'

import urllib.request
import urllib.response
import urllib.parse
import re

# # 向服务器发送一个get请求
# url = 'http://yyyyy330.blog.163.com/blog/#m=0'
# # 创建一个请求
# r = urllib.request.Request(url)
# r.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
# req = urllib.request.urlopen(url)
# print (req.status)
# b = req.read()
# BBK = b.decode('gbk')
# print (BBK)
# # print (re.findall('title="阅读全文" target="_blank" href=(.*?)/">', BBK))


"""
http://api.blog.163.com/yyyyy330/dwr/call/plaincall/BlogBeanNew.getBlogs.dwr
Request Method:POST

Content-Type:text/plain

callCount=1
scriptSessionId=${scriptSessionId}187
c0-scriptName=BlogBeanNew
c0-methodName=getBlogs
c0-id=0
c0-param0=number:134612310
c0-param1=number:20
c0-param2=number:10
batchId=935758
抓取网易博客读者信息的，请求的是：VisitBeanNew.getBlogReaders.dwr，
抓取博客内容则请求：BlogBeanNew.getBlogs.dwr
"""
url = 'http://api.blog.163.com/yyyyy330/dwr/call/plaincall/BlogBeanNew.getBlogs.dwr'
r = urllib.request.Request(url)
r.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
r.add_header('Content-Type', 'text/plain')

paraDict = {
    'callCount'      :   '1',
    'scriptSessionId':   '${scriptSessionId}187',
    'c0-scriptName'  :   'BlogBeanNew',
    'c0-methodName'  :   'getBlogs',
    'c0-id'          :   '0',
    'c0-param0'      :   '134612310',
    'c0-param1'      :   '40',
    'c0-param2'      :   '10',
    'batchId'        :   '251561'
}
paraDict['c0-param0'] = "number:" + str(11341582)
paraDict['c0-param1'] = "number:" + str(10)
paraDict['c0-param2'] = "number:" + str(1)
req = urllib.request.urlopen(url)
bbk = req.read()
print (bbk)


