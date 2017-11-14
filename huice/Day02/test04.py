lst=[1, 2, 3]
lst.append(4)
print lst

lst2 = [1, 2, 3, 4, 5, 2, 3, 1, 2, 3, 42, 1, 2, 3, 5]
count = lst2.count(1)
print count

lst3 = ['python', 'java', 'ruby']
lst4 = [2015, 2016, 2017]
lst3.extend(lst4)
print lst3

numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print numbers

lst5 = ['Me', 'and', 'my', 'broken']
index = lst5.index('my')
print index

lst6=[1,2,3,4,5,6,7,8]
print lst6.pop()
print lst6
print lst6.pop(-3)
print lst6

lst7 = list('hello')
print lst7.remove('l')
print lst7

lst8 = [1, 2, 3, 5, 6, 7]
print lst8.reverse()
print lst8

lst8 = [7, 6, 5, 3, 2, 1]
result = list(reversed(lst8))
print result

lst9 = [3, 5, 7, 3, 1, 2, 4]
lst10 = lst9[:]
lst10.sort()
print lst9
print lst10

lst11 = [3, 5, 2, 1, 7, 4, 8, 9, 3]
lst12 = sorted(lst11)
print lst11
print lst12


A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
print id(A)
A = A + B
print A
print id(A)

C = [1, 2, 3, 4]
D = [5, 6, 7, 8]
print id(C)
C += D
print C
print id(C)

E = ['Hi!']
F = E*4
print F
print id(E),id(F)


