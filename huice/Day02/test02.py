tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
tup3 = tup1 + tup2;
print tup3

tup4 = tup1 * 3;
print tup4

tup5 = tuple([1,2,3])
tup6 = tuple('abc')
print tup5, tup6

t = ((1, 2, 3),(4, 5, 6))
print  t[1][2]

t = (1, 2, 3, ['A', 'B', 'C'])
print id(t)
t[3][0] = 'D'
t[3][1] = 'E'
t[3][2] = 'F'
print id(t)
print t is t
print t