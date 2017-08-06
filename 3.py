import pycurl
import StringIO
import urllib
import json
f = open('3.txt')
a = f.read()
f.close
f = open('4.txt')
b = f.read()
f.close
url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
post_data_dic = {"api_key":"BLqiunQwr220JeP62vThLVNYC-J9QfMU","api_secret":"RSuIlaas8sMht4nlf9iwFCYUZov-cpO2","face_token1":a,"face_token2":b}
crl = pycurl.Curl()
crl.setopt(pycurl.VERBOSE,1)
crl.setopt(pycurl.FOLLOWLOCATION, 1)
crl.setopt(pycurl.MAXREDIRS, 5)
crl.setopt(pycurl.CONNECTTIMEOUT, 60)
crl.setopt(pycurl.TIMEOUT, 300)
crl.setopt(pycurl.HTTPPROXYTUNNEL,1)
crl.fp = StringIO.StringIO()
crl.setopt(pycurl.USERAGENT, "Z")
crl.setopt(crl.POSTFIELDS, urllib.urlencode(post_data_dic))
crl.setopt(pycurl.URL, url)
crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
crl.perform()
print crl.fp.getvalue()
z = crl.fp.getvalue()
f=open('r.json','w+')
f.write(z)
f.close
