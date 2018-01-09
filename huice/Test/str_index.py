# encoding:utf-8
string = 'abcabcdsf'

def re_index(str):
    for x in str:
        if str.count(x) == 1:
            return x, str.index(x)
m,n = re_index(string)
print '字符{}，下标{}'.format(m,n)


# def find_str(string):
#     for x in string:
#         if string.count(x) == 1:
#             return x, string.index(x)
#
# m,n = find_str(string)
# print '字符是{}下标是{}'.format(m,n)