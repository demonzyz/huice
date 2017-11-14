list1 = [1, 2, 3, 4, 5 ];
list2 = ["a", "b", "c", "d"];
list3 = ['python', 'java', 1997, 2000];
print list3
print type(list3)

print list3[0],list3[1],list3[2]
print list3[0:3]
print list3[1:3]
print list3[0:]
print list3[:3]
print list3[::-1]

list3[3] = 2001
# list3[4] = 2001  error
print list3

list3[2:] = [2017, 2017]
print list3

list4 = [2017, 2018, 2019]
print len(list3)
list3[2:] = list4
print list3
print len(list3)

list5 = [2017]
print len(list3)
print id(list3)
list3[:] = list5
print len(list3)

list3[:] = []
print list3
print len(list3)

list6 = [1, 2, 7]
list6[2:2] = [3, 4, 5, 6]
print list6

list7 = [1, 2, 7]
list7[2] = [3, 4, 5, 6]
print list7

list8 = [1, 2, 3, 4, 5, 6, 7, 8]
list8[5:] = []
print list8

print len(list8)
del list8[2]
print list8
print len(list8)

# del list8
# print list8