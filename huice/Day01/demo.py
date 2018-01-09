import time
def reindex(key, target):

    while len(key)>0:
        i = 0
        if key[i]+key[i+1] == target:
            i+1,i+2
            break
        else:
            i+1,len(key)-1
    return i+1,i+2

def inindex(key, target):
    for i in key:
        for j in key:
            if i + j == target:
                return key.index(i)+1, key.index(j)+1

def dindex(key, target):
    for i in key:
        if key[key.index(i)] + key[key.index(i)+1] == target:
            return key.index(i) + 1, key.index(i) + 2

def fin_index(key, target):
    for i in range(0,len(key)):
        for j in range(i,len(key)):
            if i is not j:
                if key[i] + key[j] == target:
                    return [i + 1, j + 1]

if __name__ == '__main__':
    number = [2, 2, 11, 15]
    target = 4
    # print reindex(number,target)
    # print inindex(number,target)
    # print dindex(number, target)
    print fin_index(number, target)
    number.sort(reverse=True)
    print number
