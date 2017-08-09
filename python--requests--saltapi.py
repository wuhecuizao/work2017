#登陆返回token
import requests
import json
 
data = {'username': 'saltapi', 'password': 'ajzP$9Of@GQ', 'eauth': 'pam'}
headers = {'Accept': 'application/json'} 
r = requests.post('http://10.10.44.108:8888/login', data=data, headers=headers)
doc = json.loads(r.text)
print(doc)
token=doc['return'][0]['token']
print(token)
x=key = str(token).decode("unicode_escape").encode("utf8")
#执行函数
datax = {'client': 'local','tgt': '*','fun': 'cmd.run','arg': 'echo \"Hello world!\"','expr_form': 'glob','username': 'saltapi','password': 'ajzP$9Of@GQ', 'eauth': 'pam'}
headersx = {'X-Auth-Token': x}
print(headersx)
rr=requests.post('http://10.10.44.108:8888/run', data=datax, headers=headersx)
print(rr.text)
doc = json.loads(rr.text)
yy=doc['return'][0]
print(yy)


##第二种方式

#登陆返回token
import requests
import json
 
data = {'username': 'saltapi', 'password': 'ajzP$9Of@GQ', 'eauth': 'pam'}
headers = {'Accept': 'application/json'} 
r = requests.post('http://10.10.44.108:8888/login', data=data, headers=headers)
doc = json.loads(r.text)
print(doc)
token=doc['return'][0]['token']
print(token)
x=key = str(token).decode("unicode_escape").encode("utf8")
#执行函数
datax = {'client': 'local','tgt': '*','fun': 'cmd.run','arg': ['echo \"Hello world!\"'],'expr_form': 'glob'}
headersx = {'X-Auth-Token': x}
print(headersx)
rr=requests.post('http://10.10.44.108:8888', data=datax, headers=headersx)
print(rr.text)
doc = json.loads(rr.text)
yy=doc['return'][0]
print(yy)