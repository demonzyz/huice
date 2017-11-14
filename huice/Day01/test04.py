a = 1
b = 1
print id(a)
print id(b)
print (a is b)

a = 2;
print id(a)
print id(b)


c = "very good morning"
d = "very good morning"
print 'c',id(c)
print 'd',id(d)

c = True
d = True
print 'bool',id(c)
print 'bool',id(d)


e = [1, 2, 3]
print id(e)

e = [1, 2, 3]
print id(e)

f = [1, 2, 5]
print id(f)
f.append(4)
print id(f)

