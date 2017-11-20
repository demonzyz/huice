# coding=utf-8
import xlrd
import json

import xml.dom.minidom as asd
import xml.etree.ElementTree as et
import requests

print open('test.txt','w').write('tyutyutyutyu')

# params = {'theRegionCode': '3113'}
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# reponse = requests.post('http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityDataset', data=params,headers=headers)
# print reponse.text

# params = {'theRegionCode': '3113'}
# headers = {'Content-Type': 'text/xml; charset=utf-8'}
# reponse = requests.get('http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityDataset', params=params,headers=headers)
# print reponse.text

# params = '''<?xml version="1.0" encoding="utf-8"?>
# <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
#   <soap12:Body>
#     <getSupportCityDataset xmlns="http://WebXml.com.cn/">
#       <theRegionCode>string</theRegionCode>
#     </getSupportCityDataset>
#   </soap12:Body>
# </soap12:Envelope>
# '''
# headers = {'Content-Type': 'application/soap+xml; charset=utf-8','SOAPAction': 'http://WebXml.com.cn/getSupportCityString'}
# reponse = requests.get('http://ws.webxml.com.cn/WebServices/WeatherWS.asmx', params=params,headers=headers)
# reponse.encoding = 'utf-8'
# print reponse.text


# show_json = '''
# {"xAxis": ["business_autoFans_J", "autoAX", "autoAX_admin"],
#  "yAxis": [{"2016_08": [14, 7, 16], "2016_09": [0, 13, 12], "2016_10": [24, 15, 7]},
#            {"2016_08": [0, 0, 5], "2016_09": [32, 31, 17], "2016_10": [22, 22, 9]},
#            {"2016_08": [0, 7, 10], "2016_09": [0, 0, 0], "2016_10": [5, 13, 2]}]}
# '''
#
# def search_by_month(data,month):
#     show_data = json.loads(data)
#     project_name = show_data['xAxis']
#     bug_total = []
#     for data in show_data['yAxis']:
#         sum = 0
#         if month < 10:
#             month = '0' + str(month)
#         else:
#             month = str(month)
#         for bug in data['2016_%s' % month]:
#             sum += int(bug)
#         bug_total.append(sum)
#     data_total = dict(zip(project_name, bug_total))
#     return data_total
#
# print search_by_month(show_json,8)


# show_data = json.loads(show_json)
# print type(show_data)


# print show_data
# print show_data['xAxis']
# for data in show_data['yAxis']:
#     print data
#     for bug in data['2016_08']:
#         print bug
#
# def search_by_month(data, month):
#     show_data = json.loads(data)
#     project_name = show_data['xAxis']
#     bug_number = []
#     for data in show_data['yAxis']:
#         sum = 0
#         if month<10:
#             month = '0' + str(month)
#         else:
#             month = str(month)
#
#         for bug in data['2016_%s' % month]:
#             sum += int(bug)
#         bug_number.append(sum)
#
#     bug_total = dict(zip(project_name, bug_number))
#     return bug_total
#
# print search_by_month(show_json, '09')

# r_list = asd.parse('demo.xml').getElementsByTagName('title')
#
# for e in r_list:
#     print e.childNodes[0].nodeValue
#
# print et.parse('demo.xml').find('.//title[1]').text
#
#
#

#
# # 找到excel中的列放入list
# book = xlrd.open_workbook('test.xls')
# # Sheet = book.sheet_by_name('Bugs')
# Sheet = book.sheet_by_index(2)
# col = Sheet.col_values(0)
#
# #遍历list,去重
# listName = []
# for name in col:
#     if name not in listName:
#             listName.append(name)
# listName.pop(0)
# print listName
#
# #计算listName中的项目名称的总和
# data = {}
# for value in listName:
#     number = 0
#     for n in range(1,len(col)):
#         if col[n] is value:
#             number += int(Sheet.cell(n,2).value)
#     data[value] = number
#
# json_data = json.dumps(data,indent=4)
#
# print data
# print json_data
#
# print Sheet.col_values(0).index(u'autoAX')


params = {'title': '测试第一次大会', 'address': '地中海风情岛', 'time': '2017-11-20'}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post('http://127.0.0.1:8000/api/add_event', data=params, headers=headers)
print response.text

