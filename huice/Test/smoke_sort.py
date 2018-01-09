number = [1,3,5,4,7,8,9,10]


def quick_sort(aList=[]):
    if len(aList) <= 1:
        return aList
    else:
        smalllist = []
        biglist = []
        tags = []
        tag = aList[0]
        for key in aList:
            if key > tag:
                biglist.append(key)
            elif key < tag:
                smalllist.append(key)
            else:
                tags.append(key)

        smalllist = quick_sort(smalllist)
        biglist = quick_sort(biglist)
        return smalllist + tags + biglist

print quick_sort(number)







# def quick_sort(aList=[]):
#     if len(aList) <= 1:
#         return aList
#     else:
#         tag = aList[0]
#         big_list = []
#         small_list = []
#         tags = []
#         for x in aList:
#             if x > tag:
#                 big_list.append(x)
#             elif x < tag:
#                 small_list.append(x)
#             else:
#                 tags.append(x)
#
#         small_list = quick_sort(small_list)
#         big_list = quick_sort(big_list)
#
#         return small_list + tags + big_list
#
# print quick_sort(number)