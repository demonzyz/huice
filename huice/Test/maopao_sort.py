aList = [20,30,10,50]

for x in range(len(aList)-1):
    for y in range(len(aList)-x-1):
        if aList[y] > aList[y+1]:
            aList[y], aList[y+1] = aList[y+1], aList[y]
print aList

# for i in range(len(aList) - 1):
#     for j in range(len(aList)-i-1):
#         if aList[j] > aList[j+1]:
#             aList[j], aList[j+1] = aList[j+1], aList[j]
# print aList
