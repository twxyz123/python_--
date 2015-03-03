from urllib2 import Request, urlopen, URLError, HTTPError  

old_url = 'http://rrurl.cn/b1UZuP'
req = Request(old_url)
response = urlopen(req)

print 'Old url:' + old_url
print 'Real urs:' + response.geturl()

print '==============================\n'


ourl = 'http://www.baidu.com'
re = Request(old_url)
res = urlopen(re)
print 'Info():'
print res.info()
