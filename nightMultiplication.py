# coding=utf-8
number_x = 1
number_y = 1
for number_x in range(1,10,1):
    for number_y in range(1,number_x + 1,1):
        print ('%d * %d = %d    ' % (number_y , number_x , number_y * number_x)) ,
    print('\r')
