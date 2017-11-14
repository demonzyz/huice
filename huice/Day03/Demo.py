# -*- coding: UTF-8 -*-
a = {'www': 8, 'text': 10, 'over': 9, 'obtain': 1, 'an': 2, 'sample': 5, 'texts': 6, 'Catalan': 3, 'books': 7, 'analyzing': 4}

print sorted(a.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

print reduce(lambda x,y:x+y, [1, 3, 5, 7, 9])

print filter(lambda x:x>5,[1, 3, 5, 7, 9])

# 定义函数
def mye( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行

try:
    mye(0)
except "Invalid level!":
    print 1
else:
    print 2