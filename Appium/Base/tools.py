import random
from Base import send_request
import re
import json




class base_tools():
    def __init__(self):
        self.mod = self.make_modile()

    def make_modile(self):
        abc = '110'
        for i in  range(8):
            ran = random.randint(0,9)
            modile = abc +str(ran)
            abc = modile

        return abc

    def get_yanzhengma(self):
        b = json.loads(send_request.Nice_request().post_request(url=url,head=headers,data=payload,proxies=None).content)['rows'][0]['params']
        c = re.search('\d+',b)

        return c.group()


a = base_tools().make_modile()
mod = a
url = "http://www.oneniceapp.com/mis/Smsmsg/getsmsmangerlist"
payload = {'search': ' {"mobile":'+ mod +',"table_index":"current","app":"nice"}',
'page': ' 1',
'rows': ' 10'}
headers = {
  'Cookie':'nuid=CgoKDWDujA8yCY6/P6F2Ag==; ci_session=a%3A8%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22bb165bb85fbff62535460e343b47d2b6%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22123.124.235.18%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_15_7%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F91.0.4472.164+Safari%2F537.3%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1628148630%3Bs%3A7%3A%22user_id%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22admin_id%22%3Bs%3A3%3A%22974%22%3Bs%3A10%3A%22admin_name%22%3Bs%3A8%3A%22hudongqi%22%3Bs%3A11%3A%22expire_time%22%3Bi%3A1628321430%3B%7Ddc8f822fc876722878dc270a8f4da697; nuid=CgoKPV88x2RpPn1fLL4RAg==; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%222b6cda80f7fbb54c6d8f38d94b262525%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22123.124.235.18%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A21%3A%22PostmanRuntime%2F7.26.3%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1628149741%3Bs%3A11%3A%22expire_time%22%3Bi%3A1628322541%3B%7D39ce4cf2e25ff030595c15c1fe20e03d'
}

