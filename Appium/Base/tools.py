import random
from Base import send_request
import re
import json
from Base import read_yaml



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
url = read_yaml.ReadYaml().get_value('init.yaml','yanzhengma.url')
payload = {'search': ' {"mobile":'+ mod +',"table_index":"current","app":"nice"}','page': ' 1','rows': ' 10'}
headers = read_yaml.ReadYaml().get_value('init.yaml','yanzhengma.headers')

