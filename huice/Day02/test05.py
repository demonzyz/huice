

# str_list= ['c', 'c#', 'java', 'python', 'ruby', 'javascript']
# str_list.sort()
# print str_list
#
# str_list.sort(key = int, reverse=True)
# print str_list

# nums = [2, 3, 4, 5, 6, 78, 4, 3, 3, 4, 5, 8, 9]
# nums.sort()
# print nums
#
# nums.sort(reverse=True)
# print nums
#
#
def mysort(x):
    return (x.isdigit() and int(x)%2==0, x.isdigit(), x.isupper(), x.islower(), x)

source = 'SorTing1234'

source_list = list(source)
source_list.sort(key = mysort)
result = ''.join(source_list)
print result


#
# # result = ''.join(sorted(source, key=lambda x:(x.isdigit() and int(x)%2==0, x.isdigit(), x.isupper(), x.islower(), x)))
# # print result
#
# # [x for x in y]
# x=[1,2,3,4]
# y=[5,6,7,8]
# print [a + b for a in x for b in y if a%2 == 0 and b%2 ==0]
#
# z = [[1,2],[3,4],[5,6]]
# print [j*2 for i in z for j in i ]
#
# a=[1, 2, 3, 4, 5, 6]
# print [a[x]+3 for x in range(len(a)) if (x+1)%2 == 0]
#
#
# # quchong
# list_1 = [7, 2, 3, 1, 2, 4, 5, 7, 1, 7]
# list_new = []
# for i in list_1:
#     if i not in list_new:
#         list_new.append(i)
# print list_new
#
# # 2
# print {}.fromkeys(list_1).keys()
#
# # 3
# print sorted(list(set(list_1)), key = list_1.index)
#
