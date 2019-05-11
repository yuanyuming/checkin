#coding=utf-8
import urllib.request
import urllib
import gzip
import http.cookiejar

def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
 
def ungzip(data):
    try:        
        print('.....')
        data = gzip.decompress(data)
        print('!')
    except:
        print(',')
    return data

def checkin(id,password):
    header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://jiji.world",
    "Referer":"https://jiji.world/signin",
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
    url = 'https://jiji.world/signin'
    opener = getOpener(header)
    postDict = {
        'email': id,
        'passwd': password,
                }
    postData = urllib.parse.urlencode(postDict).encode()
    #op = 
    opener.open(url, postData)
    #data = op.read()
    #data = ungzip(data)
    #print(data)
    url = 'https://jiji.world/user/checkin'
    #op = 
    opener.open(url,postData)
    #data = op.read()
    #data = ungzip(data)
    #print(data)
    url = 'https://jiji.world/user/logout'
    #op = 
    opener.open(url)
    pass

id = '1573836@qq.com'
password = 'yym971216?'
dict = {'yuanyumingzz@qq.com':'yym906254202?','yuanyumingzz@163.com':'yym971216?','1573836@qq.com':'yym971216?'}
for key in dict:
    checkin(key,dict[key])
    pass