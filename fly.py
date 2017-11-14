# coding=utf-8

fly = ['|','/','-','\\']

for number in range(1,2000000,1):
    for index in range(0,4,1):
        print fly[index] , '\r' ,
