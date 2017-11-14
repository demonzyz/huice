# coding=utf-8

input_year = raw_input("请输入测试年份:")

year = int(input_year)

if ((year%4 == 0 and year%100 != 0) or (year%400 == 0)):
    print('%d年是闰年!' % year)
else:
    print('%d年是平年、不是闰年!' % year)