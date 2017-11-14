# -*-coding:utf-8-*-
import json

mobile_json = "{'mts':'1380138',\
'province':'北京',\
'catName':'中国移动',\
'telString':'13801380000',\
'areaVid':'29400',\
'ispVid':'3236139',\
'carrier':'北京移动'}"

json_text = json.dumps(mobile_json, ensure_ascii=False)
print json_text

data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
d1 = json.dumps(data1,sort_keys=True)
d2 = json.dumps(data2)
d3 = json.dumps(data2,sort_keys=True)
print d1
print d2
print d3
print d1 == d2
print d1 == d3

stu1 = {'name': 'xiaoming', 'age': 20, 'height': 174.2, 'is_married': True, 'sroce': None}
json_stu1 = json.dumps(stu1)
json_stu2 = json.dumps(stu1, sort_keys=True)
print json_stu1
print json_stu2

data = {'b':789, 'c':456, 'a':123}
d1 = json.dumps(data, sort_keys=True)
d2 = json.dumps(data, sort_keys=True, indent=4)
print d1
print d2

data_indent = {"name":[{"firstName": "Brett"}, {"lastName": "McLaughlin"}], "age":18}
d3 = json.dumps(data_indent, sort_keys=True)
d4 = json.dumps(data_indent, sort_keys=True, indent=4)
print d3
print d4

d5 = json.dumps(data_indent, separators=('!','?'))
print d5
d6 = json.dumps(data_indent, separators=('  ,  ', '  :  '), indent=4)
print d6

data_obj = {
    "北京市": {
        "朝阳区": ["三里屯", "望京", "国贸"],
        "海淀区": ["五道口", "学院路", "后厂村"],
        "东城区": ["东直门", "崇文门", "王府井"],
    },
    "上海市": {
        "静安区": [],
        "黄浦区": [],
        "虹口区": [],
    }
}

s_dumps = json.dumps(data_obj, sort_keys=True, indent=4, ensure_ascii=False)
print(s_dumps)

with open("d:/data.json", "w") as f_dump:
    s_dump = json.dump(data_obj, f_dump, ensure_ascii=False)
print(s_dump)



# 自定义对象
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return '<MyObj(%s)(%d)>' % (self.name, self.age)

obj = Student('tiantian', 50)

try:
    print json.dumps(obj)
except TypeError, err:
    print 'ERROR:', err

#转换函数
def convert_to_builtin_type(obj):
    print 'default(', repr(obj), ')'
    # 把Student对象转换成dict类型的对象
    d = { 'name':obj.name,
          'age':obj.age,
        }
    d.update(obj.__dict__)
    return d

print json.dumps(obj, default=convert_to_builtin_type)