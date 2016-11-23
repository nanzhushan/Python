#coding:utf8
#结论:   json.dumps : dict转成str
#json.loads:str转成dict

import json
d1 = {1:2,3:5}

#测试json.dumps
d2 = json.dumps(d1)
print type(d2),d2

#测试json的loads
d3 = json.loads(d2)
print type(d3),d3
