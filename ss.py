# -*- coding:utf8 -*-

import urllib2

response = urllib2.urlopen("http://boafanx.tabboa.com/boafanx-ss/")
html = response.read()
print(html[:20000])