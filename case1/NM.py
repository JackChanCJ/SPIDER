# coding=utf-8
__author__ = 'JACK_CHAN'

import urllib.request

url = 'http://ke.qq.com'
r = urllib.request.Request(url)
req = urllib.request.urlopen(url)
print (req.geturl())
print (type(req.status))





def main():
    pass


if __name__ == '__main__':
    main()