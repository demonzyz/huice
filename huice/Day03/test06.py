
a = ['adam', 'LISA', 'barT']
print map(lambda x: x.capitalize(), a)
print map(lambda x: x[:1].upper()+x[1:].lower(), a)

b = [1, 2, 3, 4, 5]
def sum(x):
    return reduce(lambda i, j: i*j, x)

print sum(b)

