import requests
import json

proxies = {'http':'http://192.168.74.85:8888','https':'http://192.168.74.85:8888'}
class Nice_request():
    def get_request(self,url,data,cookie = None):
        get1 = requests.get(url=url,params=data,cookies=cookie)
        return get1

    def post_request(self,url,head,data,proxies):
        post1 = requests.post(url=url,headers=head,data=data,proxies=proxies,verify=False)

        return post1
